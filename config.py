##OPEN API STUFF
OPENAI_API_KEY = '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'



## FLASK STUFF
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "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"


config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}
