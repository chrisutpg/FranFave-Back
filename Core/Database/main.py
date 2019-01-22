# This file contains the actions for the database transactions

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from dbdevconfig import DB_URI

# Create the Base
Base = declarative_base()

# Create the database engine
engine = create_engine(URL(**DB_URI))

# Create the session
Session = sessionmaker(bind=engine)
db = Session()

class Test(Base):
    __tablename__ = 'Test'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(32))


Test.__table__.create(engine)