from flask import Blueprint, jsonify, redirect, render_template, request, url_for
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from app import db
from app.models import Task


bp = Blueprint("tasks", __name__)
ALLOWED_STATUSES = {"pending", "done"}


def validate_task_form(include_status=False):
    title = request.form.get("title", "").strip()
    description = request.form.get("description", "").strip()
    status = request.form.get("status", "pending")

    if len(title) < 3:
        return None, "Judul wajib diisi minimal 3 karakter."
    if len(title) > 100:
        return None, "Judul maksimal 100 karakter."
    if len(description) > 500:
        return None, "Catatan maksimal 500 karakter."
    if include_status and status not in ALLOWED_STATUSES:
        return None, "Status tugas tidak valid."

    return {
        "title": title,
        "description": description or None,
        "status": status,
    }, None


@bp.get("/health")
def health():
    try:
        db.session.execute(text("SELECT 1"))
    except SQLAlchemyError:
        db.session.rollback()
        return jsonify(status="unhealthy", database="unavailable"), 503

    return jsonify(status="healthy", database="connected")


@bp.get("/")
def index():
    tasks = Task.query.order_by(Task.created_at.desc()).all()
    return render_template("index.html", tasks=tasks)


@bp.post("/tasks")
def create_task():
    values, error = validate_task_form()
    if error:
        tasks = Task.query.order_by(Task.created_at.desc()).all()
        return (
            render_template(
                "index.html",
                tasks=tasks,
                form_data=request.form,
                form_error=error,
            ),
            400,
        )

    task = Task(title=values["title"], description=values["description"])
    db.session.add(task)
    db.session.commit()
    return redirect(url_for("tasks.index", created="1"))


@bp.get("/tasks/<int:task_id>/edit")
def edit_task(task_id):
    task = db.get_or_404(Task, task_id)
    return render_template("edit.html", task=task)


@bp.post("/tasks/<int:task_id>/update")
def update_task(task_id):
    task = db.get_or_404(Task, task_id)
    values, error = validate_task_form(include_status=True)
    if error:
        return (
            render_template(
                "edit.html",
                task=task,
                form_data=request.form,
                form_error=error,
            ),
            400,
        )

    task.title = values["title"]
    task.description = values["description"]
    task.status = values["status"]
    db.session.commit()
    return redirect(url_for("tasks.index", updated="1"))


@bp.post("/tasks/<int:task_id>/delete")
def delete_task(task_id):
    task = db.get_or_404(Task, task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("tasks.index", deleted="1"))
