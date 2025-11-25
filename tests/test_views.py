"""Tests for application views."""
import pytest


def test_index_redirects_to_login_when_not_logged_in(client):
    """Test that index redirects to login when user is not logged in."""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Login" in response.data


def test_index_shows_home_when_logged_in(client):
    """Test that index shows home page when user is logged in."""
    with client.session_transaction() as sess:
        sess["logged_in"] = True
    response = client.get("/")
    assert response.status_code == 200
    assert b"Flask Is Awesome" in response.data


def test_about_page(client):
    """Test that about page renders correctly."""
    response = client.get("/about")
    assert response.status_code == 200
    assert b"The About Page" in response.data


def test_contact_page(client):
    """Test that contact page renders correctly."""
    response = client.get("/contact")
    assert response.status_code == 200
    assert b"The Contact Page" in response.data


def test_login_page_get(client):
    """Test that login page renders on GET request."""
    response = client.get("/login")
    assert response.status_code == 200
    assert b"Login" in response.data


def test_login_with_invalid_credentials(client):
    """Test login with invalid credentials."""
    response = client.post(
        "/login",
        data={"username": "wrong", "password": "wrong"},
        follow_redirects=False,
    )
    assert response.status_code == 200
    assert b"Invalid Credentials" in response.data


def test_login_with_valid_credentials(client):
    """Test login with valid credentials."""
    response = client.post(
        "/login",
        data={"username": "admin", "password": "admin"},
        follow_redirects=True,
    )
    assert response.status_code == 200
    with client.session_transaction() as sess:
        assert sess.get("logged_in") is True


def test_logout(client):
    """Test logout functionality."""
    with client.session_transaction() as sess:
        sess["logged_in"] = True
    response = client.get("/logout", follow_redirects=True)
    assert response.status_code == 200
    with client.session_transaction() as sess:
        assert sess.get("logged_in") is None
