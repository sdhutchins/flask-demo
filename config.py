"""Configuration settings for the Flask application."""
import os
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).parent

# Enable Flask's debugging features. Should be False in production
DEBUG = os.getenv("FLASK_DEBUG", "True").lower() == "true"

# Secret key for session management
SECRET_KEY = os.getenv("SECRET_KEY", os.urandom(32).hex())
