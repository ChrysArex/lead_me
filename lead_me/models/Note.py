from sqlalchemy import Column, Integer, String, ForeignKey, Float
from werkzeug.security import generate_password_hash
from ..db import Base
from Matiere import Matiere
from User import User
from uuid import uuid4

class Note(Base):
    """Note model to map the notes table
    """
    __tablename__ = 'notes'
    id_matiere = Column(String(128), ForeignKey(Matiere.Matiere), nullable=False)
    id_user = Column(String(128), ForeignKey(User.User), nullable=False)
    note = Column(Float(), nullable=False)

    def __init__(self, id_matiere, id_user, note):
        """Initiate the model object with column values
        """
        self.id_matiere = id_matiere
        self.id_user = id_user
        self.note = note

    def __str__(self):
        """Return a string representation of a Note
        """
        return "Note: {}".format(self.moyennecalc)

    def __repr__(self):
        """Return a string representation of a Note
        """
        return "Note: {}".format(self.moyennecalc)