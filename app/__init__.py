"""Flask application factory."""
from flask import Flask
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def create_app() -> Flask:
    """
    Create and configure the Flask application.

    Returns:
        Flask: Configured Flask application instance.
    """
    app = Flask(__name__, instance_relative_config=True)

    # Load configuration from config.py
    app.config.from_object("config")

    # Register blueprints/views
    from app import views

    app.register_blueprint(views.bp)

    return app


# Create the app instance
app = create_app()