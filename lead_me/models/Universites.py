from sqlalchemy import Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from werkzeug.security import generate_password_hash
from ..db import db
from uuid import uuid4
from datetime import datetime

class Universite(db.Model):
    """Serie model to map the serie table
    """
    __tablename__ = 'universite'
    id_universite = mapped_column(String(128), primary_key=True, nullable=False)
    nom = mapped_column(String(10), nullable=False)
    created_at = mapped_column(DateTime, default=datetime.now())
    updated_at = mapped_column(DateTime, default=datetime.now())
    deleted_at = mapped_column(DateTime, nullable=True)
    code = mapped_column(String(128), nullable=True)

    def __init__(self, nom):
        """Initiate the model object with column values
        """
        self.id_universite = str(uuid4())
        self.nom = nom
        self.created_at = datetime.now()

    def __str__(self):
        """Return a string representation of a serie
        """
        return "Universite: {}".format(self.nom)

    def __repr__(self):
        """Return a string representation of a serie
        """
        return "Universite: {}".format(self.nom)
