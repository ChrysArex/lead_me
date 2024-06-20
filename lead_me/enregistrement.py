"""Defini les fonctions pour l'enregistrement et le traitement des notes
"""
from flask import (
        Blueprint, url_for, redirect, request, render_template
        )
from flask_login import login_required, current_user
from .db import db
from .models.Matiere import Matiere
from .models.Serie import Serie
from .models.Moyenne import Moyenne
from .models.Filiere import Filiere
notes_bp = Blueprint("notes", __name__, url_prefix="/notes")

@notes_bp.route("/traiter", methods=("GET", "POST"))
@login_required
def traiter():
    serie = Serie.query.filter_by(nom=current_user.serie).first()
    matieres = serie.matiere
    return render_template("enregistrement.html", matieres=matieres)

@notes_bp.route("/resultat", methods=["POST"])
def resultat():
    serie = Serie.query.filter_by(nom=current_user.serie).first()
    filieres = serie.filiere
    avg, total_coeff, prev = 0, 0, 0
    moyennes = Moyenne.query.filter_by(id_user=current_user.id).order_by(Moyenne.moyennecalc.desc()).all()
    if len(moyennes) == 0:
        for filiere in filieres:
            matieres = filiere.matiere
            for matiere in filiere.matiere:
                total_coeff += int(matiere.coefficient)
                avg += matiere.coefficient * int(request.form.get(str(matiere.nom)))
            avg = avg / total_coeff
            moyenne = Moyenne(id_filiere=filiere.id_filiere, id_user=current_user.id, moyennecalc=avg)
            moyennes.append(moyenne)
            db.session.add(moyenne)
            db.session.commit()
            avg, total_coeff = 0, 0
        moyennes = Moyenne.query.filter_by(id_user=current_user.id).order_by(Moyenne.moyennecalc.desc()).all()

    filieres = []
    noms = []
    for f in moyennes:
            fill = Filiere.query.filter_by(id_filiere=f.id_filiere).first()
            if fill.nom not in noms:
                noms.append(fill.nom)
                filieres.append(fill)
    nbr = len(filieres)

    return render_template("result.html", moyennes=moyennes, filieres=filieres, nbr=nbr)
