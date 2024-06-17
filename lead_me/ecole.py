"""
Routes and cruds fonction of Ecole entity
"""

from flask import (request, jsonify, redirect, url_for, render_template, Blueprint)
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from lead_me.models.Ecole import Ecole
from .db import db

ecoles_bp = Blueprint('ecoles', __name__, url_prefix="/ecoles")

class CSRFProtectForm(FlaskForm):
    pass

class CreateEcoleForm(FlaskForm):
    """
    Cette classe se charge de créer le formulaire et ses champs
    et de faire la validation des donnés
    """
    ecole_name = StringField("Nom", validators=[DataRequired(message="Le champ ne doit pas être vide.")])
    ecole_code = StringField("Code", validators=[DataRequired(message="Le champ ne doit pas être vide.")])

    def validate_ecole_name(self, field):
        if Ecole.query.filter_by(nom=field.data).first():
            raise ValidationError("Un rôle avec ce nom existe déjà.")
    def validate_ecole_code(self, field):
        if Ecole.query.filter_by(code=field.data).first():
            raise ValidationError("Une Université avec ce code existe déjà.")

    submit = SubmitField('Soumettre')