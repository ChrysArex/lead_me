"""Define function views for login and register
"""
from flask import (
        Blueprint, url_for, redirect, request, render_template
        )
from .models import User
from .db import session

                        
auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route("/register", methods=("GET", "POST"))
def register():
    if request.method == "POST":
         user = User.User(
            matricule=request.form.get("matricule"),
            prenom=request.form.get("prenom"),
            nom=request.form.get("nom"),
            email=request.form.get("email"),
            password=request.form.get("password"),
            serie=request.form.get("serie")
         )
         session.add(user)
         session.commit()
         return redirect(url_for('notes.traiter'))
    return render_template("login.html")
