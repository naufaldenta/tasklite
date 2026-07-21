from flask import Blueprint, redirect, render_template, request, url_for

from app import db
from app.models import Task


bp = Blueprint("tasks", __name__)


@bp.get("/")
def index():
    tasks = Task.query.order_by(Task.created_at.desc()).all()
    return render_template("index.html", tasks=tasks)


@bp.post("/tasks")
def create_task():
    task = Task(
        title=request.form.get("title", "").strip(),
        description=request.form.get("description", "").strip() or None,
    )
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
    task.title = request.form.get("title", "").strip()
    task.description = request.form.get("description", "").strip() or None
    task.status = request.form.get("status", "pending")
    db.session.commit()
    return redirect(url_for("tasks.index", updated="1"))


@bp.post("/tasks/<int:task_id>/delete")
def delete_task(task_id):
    task = db.get_or_404(Task, task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("tasks.index", deleted="1"))
