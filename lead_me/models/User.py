from sqlalchemy import Integer, String, ForeignKey, Date
from sqlalchemy.orm import Mapped, mapped_column
from werkzeug.security import generate_password_hash
from ..db import db
from uuid import uuid4
from datetime import datetime


class User(db.Model):
    """User model to map the users table
    """
    __tablename__ = 'users'
    id = mapped_column(String(128), primary_key=True, nullable=False)
    matricule = mapped_column(String(128), nullable=False)
    prenom = mapped_column(String(45), nullable=False)
    nom = mapped_column(String(45), nullable=False)
    email = mapped_column(String(100), nullable=True)
    password = mapped_column(String(200), nullable=False)
    role = mapped_column(String(45), nullable=False)
    serie = mapped_column(String(10), nullable=False)
    created_at = mapped_column(Date, default=datetime.now())

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
        self.created_at = datetime.now()

    def __str__(self):
        """Return a string representation of a user
        """
        return "User: {} {}".format(self.prenom, self.nom)

    def __repr__(self):
        """Return a string representation of a user
        """
        return "User: {} {}".format(self.prenom, self.nom)
