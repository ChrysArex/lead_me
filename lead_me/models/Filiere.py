from sqlalchemy import Column, Integer, String, ForeignKey, Text, Date
from sqlalchemy.orm import Mapped, mapped_column
from werkzeug.security import generate_password_hash
from ..db import Base
from .Ecole import Ecole
from uuid import uuid4
from datetime import datetime

class Filiere(Base):
    """ecole model to map the serie table
    """
    __tablename__ = 'filiere'
    id_filiere = mapped_column(String(128), primary_key=True, nullable=False)
    nom = mapped_column(String(10), nullable=False)
    debouches = mapped_column(Text(), nullable=False)
    bourses = mapped_column(Integer(), nullable=False)
    semi_bourses = mapped_column(Integer(), nullable=False)
    formule = mapped_column(String(150), nullable=False)
    categorie = mapped_column(String(20), nullable=False)
    id_ecole = mapped_column(String(128), ForeignKey(Ecole.id_ecole), nullable=False)
    created_at = mapped_column(Date, default=datetime.now())

    def __init__(self, nom, debouches, bourses, semi_bourses, formule, categorie):
        """Initiate the model object with column values
        """
        self.id_filiere = str(uuid4())
        self.nom = nom
        self.debouches = debouches
        self.bourses = bourses
        self.semi_bourses = semi_bourses
        self.formule = formule
        self.categorie = categorie
        self.created_at = datetime.now()

    def __str__(self):
        """Return a string representation of a serie
        """
        return "Ecole: {}".format(self.nom)

    def __repr__(self):
        """Return a string representation of a serie
        """
        return "Ecole: {}".format(self.nom)