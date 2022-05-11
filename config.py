import os

class Config:
    SECRET_KEY='5678'
    SQLALCHEMY_DATABASE_URI =SQLALCHEMY_DATABASE_URI = 'postgresql://eayqbjrfoytgud:66cf71c74cce1297c26bf44bab6eb1f91d812be9fb23b98f54eeb39e2f78a7df@ec2-3-231-82-226.compute-1.amazonaws.com:5432/d8kju1nsufb22n'
    
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    
    
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'pitch'
    SENDER_EMAIL = 'wangu.mwangi@student.moringaschool.com'

    
   
    @staticmethod
    def init_app(app):
        pass


    
class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI= 'postgresql://eayqbjrfoytgud:66cf71c74cce1297c26bf44bab6eb1f91d812be9fb23b98f54eeb39e2f78a7df@ec2-3-231-82-226.compute-1.amazonaws.com:5432/d8kju1nsufb22n'
    # uri = os.getenv('DATABASE_URL')
    # if uri and uri.startswith('postgres://'):
    #     uri = uri.replace('postgres://', 'postgresql://', 1)
        
    #     SQLALCHEMY_DATABASE_URI=uri 


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://eayqbjrfoytgud:66cf71c74cce1297c26bf44bab6eb1f91d812be9fb23b98f54eeb39e2f78a7df@ec2-3-231-82-226.compute-1.amazonaws.com:5432/d8kju1nsufb22n'

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://eayqbjrfoytgud:66cf71c74cce1297c26bf44bab6eb1f91d812be9fb23b98f54eeb39e2f78a7df@ec2-3-231-82-226.compute-1.amazonaws.com:5432/d8kju1nsufb22n'
    # DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}