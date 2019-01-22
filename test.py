# Testing MySql Connection

from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base

franfave_settings = {'drivername': 'mysql+pymysql',
                     'username': 'cnelson_franfave',
                     'password': 'franfavedev01!',
                     'host': '192.254.225.163',
                     'port': '3306',
                     'database': 'cnelson_franfave'}

engine = create_engine(URL(**franfave_settings))

print(URL(**franfave_settings))