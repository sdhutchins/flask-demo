"""Application entry point for development server."""
from app import app

if __name__ == "__main__":
    app.run(debug=app.config.get("DEBUG", False))
