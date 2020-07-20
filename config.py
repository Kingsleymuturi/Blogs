import os
from dotenv import load_dotenv
load_dotenv()
#from instance.config import DATABASE_URL,MAIL_USERNAME,MAIL_PASSWORD,SECRET_KEY
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    #SECRET_KEY = SECRET_KEY
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    #SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    DEBUG = True

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    DEBUG = True

config_options = {
'production':ProdConfig
}