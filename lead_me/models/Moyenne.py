from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import Mapped, mapped_column
from werkzeug.security import generate_password_hash
from ..db import Base
from Filiere import Filiere
from User import User
from uuid import uuid4

class Moyenne(Base):
    """Moyenne model to map the serie table
    """
    __tablename__ = 'moyenne'
    id_filiere = mapped_column(String(128), ForeignKey(Filiere.Filiere), nullable=False)
    id_user = mapped_column(String(128), ForeignKey(User.User), nullable=False)
    moyennecalc = mapped_column(Float(), nullable=False)
    created_at = mapped_column(Date, default=datetime.now())

    def __init__(self, id_filiere, id_user, moyennecalc):
        """Initiate the model object with column values
        """
        self.id_filiere = id_filiere
        self.id_user = id_user
        self.moyennecalc = moyennecalc
        self.created_at = datetime.now()

    def __str__(self):
        """Return a string representation of a Moyenne
        """
        return "Moyenne: {}".format(self.moyennecalc)

    def __repr__(self):
        """Return a string representation of a Moyenne
        """
        return "Moyenne: {}".format(self.moyennecalc)