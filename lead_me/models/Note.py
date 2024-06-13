from sqlalchemy import Column, Integer, String, ForeignKey, Float, Date
from sqlalchemy.orm import Mapped, mapped_column
from werkzeug.security import generate_password_hash
from ..db import Base
from .Matiere import Matiere
from .User import User
from uuid import uuid4
from datetime import datetime

class Note(Base):
    """Note model to map the notes table
    """
    __tablename__ = 'notes'
    id_note = mapped_column(String(128), primary_key=True, nullable=False)
    id_matiere = mapped_column(String(128), ForeignKey(Matiere.id_matiere), nullable=False)
    id_user = mapped_column(String(128), ForeignKey(User.id), nullable=False)
    note = mapped_column(Float(), nullable=False)
    created_at = mapped_column(Date, default=datetime.now())

    def __init__(self, id_matiere, id_user, note):
        """Initiate the model object with column values
        """
        self.id_matiere = id_matiere
        self.id_user = id_user
        self.note = note
        self.created_at = datetime.now()

    def __str__(self):
        """Return a string representation of a Note
        """
        return "Note: {}".format(self.moyennecalc)

    def __repr__(self):
        """Return a string representation of a Note
        """
        return "Note: {}".format(self.moyennecalc)