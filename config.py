import os

class Config:
    SECRET_KEY='7905'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:enter@localhost/visual'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    
    
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
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:enter@localhost/visual'
    # uri = os.getenv('DATABASE_URL')
    # if uri and uri.startswith('postgres://'):
    #     uri = uri.replace('postgres://', 'postgresql://', 1)
        
    #     SQLALCHEMY_DATABASE_URI=uri 


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:enter@localhost/visual'
    # SQLALCHEMY_DATABASE_URI = 'postgresql://eayqbjrfoytgud:66cf71c74cce1297c26bf44bab6eb1f91d812be9fb23b98f54eeb39e2f78a7df@ec2-3-231-82-226.compute-1.amazonaws.com:5432/d8kju1nsufb22n'

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:enter@localhost/visual'
    # DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}