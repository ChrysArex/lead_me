from flask import Flask, render_template
from .models import (User, Universites, Serie, Role, Note, Moyenne, Matiere, Filiere, Ecole)
import requests
import json
import os


def create_app(test_config=None):
    """configure and return our main app"""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY='dev')
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///lead_me.db"

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from .db import db
    db.init_app(app)
    with app.app_context():
        db.create_all()
    from .auth import auth_bp
    from .enregistrement import notes_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(notes_bp)
    @app.route("/home", methods=["GET"])
    def resultat():
        return render_template("frontend/landing_page.html")
    return app
