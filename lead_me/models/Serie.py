from sqlalchemy import Column, Integer, String, ForeignKey
from werkzeug.security import generate_password_hash
from ..db import Base
from uuid import uuid4

class Serie(Base):
    """Serie model to map the serie table
    """
    __tablename__ = 'serie'
    id_serie = Column(String(128), primary_key=True, nullable=False)
    nom = Column(String(10), nullable=False)

    def __init__(self, nom):
        """Initiate the model object with column values
        """
        self.id_serie = str(uuid4())
        self.nom = nom

    def __str__(self):
        """Return a string representation of a serie
        """
        return "Serie: {}".format(self.nom)

    def __repr__(self):
        """Return a string representation of a serie
        """
        return "Serie: {}".format(self.nom)