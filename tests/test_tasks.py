from app import db
from app.models import Task


def add_task(app, title="Belajar Docker", description="Baca Compose"):
    with app.app_context():
        task = Task(title=title, description=description)
        db.session.add(task)
        db.session.commit()
        return task.id


def test_index_shows_empty_state(client):
    response = client.get("/")

    assert response.status_code == 200
    assert b"Belum ada tugas" in response.data


def test_create_task(client, app):
    response = client.post(
        "/tasks",
        data={"title": "Buat Dockerfile", "description": "Pakai image slim"},
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"Tugas baru berhasil ditambah" in response.data
    with app.app_context():
        task = db.session.execute(db.select(Task)).scalar_one()
        assert task.title == "Buat Dockerfile"
        assert task.status == "pending"


def test_edit_page_shows_existing_task(client, app):
    task_id = add_task(app, title="Judul lama")

    response = client.get(f"/tasks/{task_id}/edit")

    assert response.status_code == 200
    assert b"Judul lama" in response.data


def test_update_task(client, app):
    task_id = add_task(app)

    response = client.post(
        f"/tasks/{task_id}/update",
        data={"title": "Belajar Compose", "description": "Sudah dirapihin", "status": "done"},
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"Perubahan tugas berhasil disimpan" in response.data
    with app.app_context():
        task = db.session.get(Task, task_id)
        assert task.title == "Belajar Compose"
        assert task.status == "done"


def test_delete_task(client, app):
    task_id = add_task(app, title="Tugas sementara")

    response = client.post(f"/tasks/{task_id}/delete", follow_redirects=True)

    assert response.status_code == 200
    assert b"Tugas berhasil dihapus" in response.data
    with app.app_context():
        assert db.session.get(Task, task_id) is None
