import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import URL


db = SQLAlchemy()


def _database_url():
    """Menyusun URL database dari environment variable."""
    if os.getenv("DATABASE_URL"):
        return os.environ["DATABASE_URL"]

    if os.getenv("DB_HOST"):
        user = os.getenv("POSTGRES_USER", "tasklite")
        password = os.getenv("POSTGRES_PASSWORD", "tasklite")
        host = os.getenv("DB_HOST", "db")
        port = int(os.getenv("DB_PORT", "5432"))
        name = os.getenv("POSTGRES_DB", "tasklite")
        return URL.create(
            "postgresql+psycopg",
            username=user,
            password=password,
            host=host,
            port=port,
            database=name,
        )

    return "sqlite:///tasklite.db"


def create_app(test_config=None):
    """Membuat instance aplikasi TaskLite."""
    app = Flask(__name__)
    app.config.from_mapping(
        SQLALCHEMY_DATABASE_URI=_database_url(),
        SQLALCHEMY_ENGINE_OPTIONS={"pool_pre_ping": True},
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    if test_config:
        app.config.update(test_config)

    db.init_app(app)

    from app.models import Task  # noqa: F401

    with app.app_context():
        db.create_all()

    from app.routes import bp

    app.register_blueprint(bp)

    return app
