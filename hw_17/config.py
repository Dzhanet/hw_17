import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.getcwd(), 'test.db') #абсолютный путь относительно файла config до БД
    SQLALCHEMY_TRACK_MODIFICATIONS = False
