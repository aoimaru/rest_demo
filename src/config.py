import os

class DevelopmentConfig:
    def __init__(self, URI):
        self.URI = URI

    @classmethod
    def Config(cls):
        SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8'.format(
          **{
            'user': os.getenv('DB_USER', 'root'),
            'password': os.getenv('DB_PASSWORD', 'root'),
            'host': os.getenv('DB_HOST', 'db_address'),
            'database': os.getenv('DB_DATABASE', 'sample01'),
          })

        return cls(SQLALCHEMY_DATABASE_URI)

