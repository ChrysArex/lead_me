from sqlalchemy import Column, Integer, String, ForeignKey, Text
from werkzeug.security import generate_password_hash
from ..db import Base
from Ecole import Ecole
from uuid import uuid4

class Filiere(Base):
    """ecole model to map the serie table
    """
    __tablename__ = 'filiere'
    id_filiere = Column(String(128), primary_key=True, nullable=False)
    nom = Column(String(10), nullable=False)
    debouches = Column(Text(), nullable=False)
    bourses = Column(Integer(), nullable=False)
    semi_bourses = Column(Integer(), nullable=False)
    formule = Column(String(150), nullable=False)
    categorie = Column(String(20), nullable=False)
    id_ecole = Column(String(128), ForeignKey(Ecole.ecole), nullable=False)

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

    def __str__(self):
        """Return a string representation of a serie
        """
        return "Ecole: {}".format(self.nom)

    def __repr__(self):
        """Return a string representation of a serie
        """
        return "Ecole: {}".format(self.nom)