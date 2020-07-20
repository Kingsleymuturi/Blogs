import os
from dotenv import load_dotenv
load_dotenv()
from instance.config import DATABASE_URL,MAIL_USERNAME,MAIL_PASSWORD,SECRET_KEY
class Config:
    #SECRET_KEY = os.environ.get('SECRET_KEY')
    SECRET_KEY = SECRET_KEY
    #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    #MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_USERNAME = MAIL_USERNAME
    #MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    MAIL_PASSWORD = MAIL_PASSWORD
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    DEBUG = True