"""Define function views for login and register
"""
from flask import (
        Blueprint, url_for, redirect, request, render_template
        )
from .models import User
from .db import db
from .FormValidator import RegistrationForm, LoginForm


auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route("/register", methods=("GET", "POST"))
def register():
    form = RegistrationForm(request.form)
    r_or_l = "Register"
    if request.method == "POST":
        """if not form.validate():
            return render_template("auth/register_login.html",
                                    form=form, r_or_l=r_or_l)"""
        user = User.User(
            matricule=request.form.get("matricule"),
            prenom=request.form.get("prenom"),
            nom=request.form.get("nom"),
            email=request.form.get("email"),
            password=request.form.get("password"),
            serie=request.form.get("serie")
         )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('notes.traiter'))
    return render_template("login.html")
