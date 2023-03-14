class Config(object):
    pass
    

class DevelopmentConfig(Config):
    TESTING = True

    DB_HOST = "localhost"
    DB_NAME = "letsbeelife"
    DB_USERNAME = "postgres"
    DB_PASSWORD = "root"

    SECRET_KEY = "sadfsdsdf8sdf8s7ad6f87sd6f8s7d6f8sd68f7"
    SESSION_COOKIE_SECURE = False

class ProductionConfig(Config):
    pass
        