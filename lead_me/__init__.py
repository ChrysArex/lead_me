from flask import Flask, render_template
import requests
import json
import os


def create_app(test_config=None):
    """configure and return our main app"""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY='dev')

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_db(db.Base)
    app.teardown_appcontext(db.shutdown_session)
    from .login import auth_bp
    from .enregistrement import notes_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(notes_bp)
    return app