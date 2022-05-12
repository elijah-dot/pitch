import os

class Config:
    SECRET_KEY='7905'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:rud@localhost/work'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SQLALCHEMY_DATABASE_URI = 'postgres://mchocezjfxzarl:a9b935d4e036cca5080ed17a14a954ccd97d7ba3a13027f961e36188b8efebf2@ec2-34-236-94-53.compute-1.amazonaws.com:5432/d5gamob8slp5c4'
    
    
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'pitch'
    SENDER_EMAIL = 'elijahwangu91@gmail.com'

    
   
    @staticmethod
    def init_app(app):
        pass


    
class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:rud@localhost/work'
    uri = os.getenv('DATABASE_URL')
    if uri and uri.startswith('postgres://'):
     uri = uri.replace('postgres://', 'postgresql://', 1)
        
    SQLALCHEMY_DATABASE_URI=uri 


class TestConfig(Config):
    pass
class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:rud@localhost/work'
    # DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}