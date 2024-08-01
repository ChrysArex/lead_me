"""
Routes and cruds fonction of User entity
"""

from flask import (request, jsonify, redirect, url_for, render_template, Blueprint)
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from lead_me.models.User import User
from .db import db

users_bp = Blueprint("users", __name__, url_prefix="/users")
class CSRFProtectForm(FlaskForm):
    pass

class CreateUserForm(FlaskForm):
    """
    Cette classe se charge de créer le formulaire et ses champs
    et de faire la validation des donnés
    """
    user_nom = StringField("Nom", validators=[DataRequired(message="Le champ ne doit pas être vide.")])
    user_prenom = StringField("Code", validators=[DataRequired(message="Le champ ne doit pas être vide.")])
    user_mail = StringField("Code", validators=[DataRequired(message="Le champ ne doit pas être vide.")])
    

    def validate_user_nom(self, field):
        if User.query.filter_by(nom=field.data).first():
            raise ValidationError("Un utilisateur avec ce nom existe déjà.")
    def validate_user_prenom(self, field):
        if User.query.filter_by(prenom=field.data).first():
            raise ValidationError("Un utilisateur avec ce prenom existe déjà.")
    def validate_user_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("Un utilisateur avec ce prenom existe déjà.")

    submit = SubmitField('Soumettre')
    
@users_bp.route("/", methods=["GET"])
def list_users():
    users = User.query.all()
    form = CSRFProtectForm()
    return render_template("dashboard/users/index.html", users=users, form=form)

# @users_bp.route("/create", methods=["GET", "POST"])
# def create():
#     """
#     création des user
#     """
#     form = CreateUserForm()
#     if form.validate_on_submit():
#         user= User(
#             prenom=form.user_prenom.data,
#             nom=form.user_nom.data,
#             matricule="ROOT",
#             email= form.user_mail
#         )