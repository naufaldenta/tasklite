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
