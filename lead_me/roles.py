from flask import request, jsonify, redirect, url_for, render_template
from .models import Role
"""
Routes and cruds fonction of Role entity
"""
from flask import (
        Blueprint, url_for, redirect, request, render_template
        )
roles_bp = Blueprint("roles", __name__, url_prefix="/roles")
@roles_bp.route("/roles", methods=("GET", "POST"))
def list_roles():
    roles = Role.query.all();
    return render_template("dashboard/roles/index.html", roles=roles)

@roles_bp.route("/roles/create", methods=("GET", "POST"))
def create_list():
    if request.method == "POST":
        return "<p>Actually just test</p>"
    return render_template('dashboard/roles/create.html')