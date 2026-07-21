from flask import Blueprint, render_template

from app.models import Task


bp = Blueprint("tasks", __name__)


@bp.get("/")
def index():
    tasks = Task.query.order_by(Task.created_at.desc()).all()
    return render_template("index.html", tasks=tasks)
