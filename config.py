import os 
from dotenv import load_dotenv

load_dotenv()  # Muat file .env jika ada

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    HOST     = str(os.environ.get("DB_HOST"))
    DATABASE = str(os.environ.get("DB_DATABASE"))
    USERNAME = str(os.environ.get("DB_USERNAME"))
    PASSWORD = str(os.environ.get("DB_PASSWORD"))

    # SQL ALCHEMY UNTUK DATABASE MIGRATION
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://'+ USERNAME +':'+PASSWORD + '@' + HOST + '/' + DATABASE
    SQLALCHEMY_TRACK_MODIFICATION = False
    SQLALCHEMY_RECORD_QUERY = True
    SQLALCHEMY_ECHO = True