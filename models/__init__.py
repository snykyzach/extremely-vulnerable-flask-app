from os import path
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker
from .base_model import BaseModel
from .user import User
from .registration_code import RegistrationCode

basedir = path.abspath(path.dirname(__file__))

engine: Engine = create_engine('sqlite:///' +
                               path.join(basedir, '..', 'database.db'),
                               echo=False,
                               encoding='utf8')

BaseModel.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)