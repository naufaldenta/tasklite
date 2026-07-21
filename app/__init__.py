from flask import Flask


def create_app(test_config=None):
    """Membuat instance aplikasi TaskLite."""
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY="dev-only-key",
    )

    if test_config:
        app.config.update(test_config)

    @app.get("/")
    def index():
        return "TaskLite siap"

    return app

