import os
class Config:
    '''
    General configuration parent class
    '''

    SOURCE_API_BASE_URL ='https://newsapi.org/v2/sources?category={}&apiKey={}'                  
    ARTICLE_API_NEWS_URL ='https://newsapi.org/v2/everything?sources={}&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True