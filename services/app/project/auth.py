"""TODO"""
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import (  # pylint: disable=import-error
    login_required,
    login_user,
    logout_user,
)
from werkzeug.security import check_password_hash, generate_password_hash
from project.models import User
from . import db

auth = Blueprint(
    "auth", __name__, template_folder="../templates", static_folder="../static"
)


@auth.route("/login", methods=["GET", "POST"])
def login():
    """LogIn Page"""
    if request.method == "GET":
        return render_template("login.html")
    email = request.form.get("email")
    password = request.form.get("password")
    remember = bool(request.form.get("remember"))

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash("Please check your login details and try again.")
        return redirect(url_for("auth.login"))
    login_user(user, remember=remember)
    return redirect(url_for("main.games"))


@auth.route("/signup", methods=["GET", "POST"])
def signup():
    """SignUp Page"""
    if request.method == "GET":
        return render_template("signup.html")
    email = request.form.get("email")
    name = request.form.get("name")
    password = request.form.get("password")

    user = User.query.filter_by(email=email).first()

    if user:
        flash("Email address already exists")
        return redirect(url_for("auth.signup"))

    new_user = User(
        email=email,
        name=name,
        password=generate_password_hash(password, method="sha256"),
    )

    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for("auth.login"))


@auth.route("/logout")
@login_required
def logout():
    """LogOut Page"""
    logout_user()
    return redirect(url_for("main.index"))
