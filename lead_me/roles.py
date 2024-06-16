from flask import request, jsonify, redirect, url_for, render_template
from lead_me.models.Role import Role
from .db import db
"""
Routes and cruds fonction of Role entity
"""
from flask import (
        Blueprint, url_for, redirect, request, render_template
        )
roles_bp = Blueprint("roles", __name__, url_prefix="/roles")

@roles_bp.route("/", methods=["GET"])
def list_roles():
        
    roles = Role.query.all()
    return render_template("dashboard/roles/index.html", roles=roles)

@roles_bp.route("/create", methods=("GET", "POST"))
def create():
    error = None
    if request.method == "POST":
        role_name = request.form['role'].strip()  #
        if not role_name:
            error = "Le champ ne doit pas être vide."
        else:
            new_role = Role(role_name)
            from .db import db
            db.session.add(new_role)
            db.session.commit()
            return redirect(url_for('roles.list_roles'))

    return render_template('./dashboard/roles/create.html', error=error)

@roles_bp.route("/edit<string:role_id>", methods=("GET", "POST"))
def edit(role_id):
    role = Role.query.get_or_404(role_id)
    if request.method == "POST":
        role_name = request.form['role'].strip()
        if not role_name:
            error = "Le champ ne doit pas être vide."
            return render_template("dashboard/roles/edit.html", role=role, error=error)
        else:
            role.nom = role_name
            db.session.commit()
            return redirect(url_for('roles.list_roles'))
    return render_template("dashboard/roles/edit.html", role=role)

@roles_bp.route("/delete/<string:role_id>", methods=["POST"])
def delete_role(role_id):
    role = Role.query.get_or_404(role_id)
    db.session.delete(role)
    db.session.commit()
    return redirect(url_for('roles.list_roles'))