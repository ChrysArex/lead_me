from sqlalchemy import Column, Integer, String, ForeignKey
from werkzeug.security import generate_password_hash
from ..db import Base
from uuid import uuid4

class Role(Base):
    """Role model to map the role table
    """
    __tablename__ = 'role'
    id_role = Column(String(128), primary_key=True, nullable=False)
    nom = Column(String(10), nullable=False)

    def __init__(self, nom):
        """Initiate the model object with column values
        """
        self.id_role = str(uuid4())
        self.nom = nom

    def __str__(self):
        """Return a string representation of a Role
        """
        return "Role: {}".format(self.nom)

    def __repr__(self):
        """Return a string representation of a Role
        """
        return "Role: {}".format(self.nom)