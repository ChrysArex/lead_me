from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from werkzeug.security import generate_password_hash
from Serie import Serie
from ..db import Base
from uuid import uuid4

class Matiere(Base):
    """Serie model to map the matiere table
    """
    __tablename__ = 'matiere'
    id_matiere = mapped_column(String(128), primary_key=True, nullable=False)
    nom = mapped_column(String(10), nullable=False)
    id_serie = mapped_column(String(128), ForeignKey(Serie.id_serie), nullable=False)
    created_at = mapped_column(Date, default=datetime.now())

    def __init__(self, nom):
        """Initiate the model object with column values
        """
        self.id = str(uuid4())
        self.nom = nom
        self.created_at = datetime.now()

    def __str__(self):
        """Return a string representation of a matiere
        """
        return "Matiere: {}".format(self.nom)

    def __repr__(self):
        """Return a string representation of a matiere
        """
        return "Matiere: {}".format(self.nom)