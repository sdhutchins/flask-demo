"""Application routes and views."""
from typing import Union

from flask import Blueprint, Response, flash, redirect, render_template, request, session, url_for

bp = Blueprint("main", __name__)


@bp.route("/")
def index() -> str:
    """
    Render the home page or login page based on session state.

    Returns:
        str: Rendered HTML template.
    """
    if not session.get("logged_in"):
        return render_template("login.html")
    return render_template("index.html")


@bp.route("/about")
def about() -> str:
    """
    Render the about page.

    Returns:
        str: Rendered HTML template.
    """
    return render_template("about.html")


@bp.route("/contact")
def contact() -> str:
    """
    Render the contact page.

    Returns:
        str: Rendered HTML template.
    """
    return render_template("contact.html")


@bp.route("/login", methods=["GET", "POST"])
def login() -> Union[str, Response]:
    """
    Handle user login.

    Returns:
        Union[str, Response]: Rendered login template or redirect to index.
    """
    error = None
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()

        if username != "admin" or password != "admin":
            error = "Invalid Credentials. Please try again."
        else:
            session["logged_in"] = True
            flash("Successful login.")
            return redirect(url_for("main.index"))

    return render_template("login.html", error=error)


@bp.route("/logout")
def logout() -> Response:
    """
    Handle user logout.

    Returns:
        Response: Redirect to index page.
    """
    session.pop("logged_in", None)
    flash("You have been logged out.")
    return redirect(url_for("main.index"))
