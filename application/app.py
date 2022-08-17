from flask import Flask, request
from flask_restx import Api, Resource
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() #объявим БД

def create_app():
    """функция, объявляющая фласк"""

    app = Flask(__name__)

    with app.app_context():
        app.config.from_object('config.Config')
        api = Api(app) #создаем объект App
        app.config['api'] = api
        from application import routes
    db.init_app(app)  # инициализация БД
    return app




