"""Defini les fonctions pour l'enregistrement et le traitement des notes
"""
from flask import (
        Blueprint, url_for, redirect, request, render_template
        )

notes_bp = Blueprint("notes", __name__, url_prefix="/notes")

@notes_bp.route("/traiter", methods=("GET", "POST"))
def traiter():
    return render_template("enregistrement.html")

@notes_bp.route("/resultat", methods=("GET", "POST"))
def resultat():
    return render_template("dashboard/user/index.html")