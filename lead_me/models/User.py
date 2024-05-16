from sqlalchemy import Column, Integer, String, ForeignKey
from werkzeug.security import generate_password_hash
from ..db import Base
from uuid import uuid4


class User(UserMixin, Base):
    """User model to map the users table
    """
    __tablename__ = 'users'
    id = Column(String(128), primary_key=True, nullable=False)
    matricule = Column(String(128), nullable=False)
    prenom = Column(String(45), nullable=False)
    nom = Column(String(45), nullable=False)
    email = Column(String(100), nullable=True)
    password = Column(String(200), nullable=False)
    role = Column(String(200), nullable=False)
    serie = Column(String(10), nullable=False)

    def __init__(self, prenom, nom, matricule, email, password, serie):
        """Initiate the model object with column values
        """
        self.id = str(uuid4())
        self.prenom = prenom
        self.nom = nom
        self.matricule = matricule
        self.email = email
        self.password = generate_password_hash(password)
        self.role = "user"
        self.serie = serie

    def __str__(self):
        """Return a string representation of a user
        """
        return "User: {} {}".format(self.prenom, self.nom)

    def __repr__(self):
        """Return a string representation of a user
        """
        return "User: {} {}".format(self.prenom, self.nom)