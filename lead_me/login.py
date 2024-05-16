"""Define function views for login and register
"""
from flask import (
        Blueprint, url_for, redirect, request, render_template
        )

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route("/register", methods=("GET", "POST"))
def register():
    return render_template("login.html")