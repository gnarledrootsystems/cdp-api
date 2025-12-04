class Config(object):
    SECRET_KEY = ""
    TESTING = False
    
class DevelopmentConfig(Config):
    DEBUG = True
    MONGO_DB = ""
    MONGO_URI = ""
    
class TesetingConfig(Config):
    TESTING = True    
    
class ProductionConfig(Config):
    DEBUG = False
    MONGO_DB = ""
    MONGO_URI = ""