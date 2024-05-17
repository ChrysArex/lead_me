"""Define useful functions to interact with the database
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, scoped_session, sessionmaker

engine = create_engine("sqlite:///leadme.db")
session = scoped_session(sessionmaker(
                            autocommit=False,
                            autoflush=False,
                            bind=engine
                        ))
Base = declarative_base()

def init_db(Base):
    """initialize the database by mapping the defined models with database
    tables
    """
    from . import models
    Base.metadata.create_all(engine)

def shutdown_session(exception=None):
    session.remove()