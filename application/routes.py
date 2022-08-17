#хранилище роутов

from flask import current_app as app, request
from flask_restx import Api, Namespace, Resource
from application.models import db
from application import models, schema

api: Api = app.config['api'] #экземпляр класса Api

movies_ns: Namespace = api.namespace('movies') #создаем неймспейс для фильмов с префиксом movies
directors_ns: Namespace = api.namespace('directors')
genre_ns: Namespace = api.namespace('genres')

movies_schema = schema.Movie(many=True) #может принимать список значений, поэтому True
movie_schema = schema.Movie() #объект класса схема

directors_schema = schema.Director(many=True)
director_schema = schema.Director()

genres_schema = schema.Genre(many=True)
genre_schema = schema.Genre()

@movies_ns.route('/')
class MoviesView(Resource):

    def get(self):
        """метод для получения всех фильмов"""

        movies_query = db.session.query(models.Movie) #запрос в БД
        args = request.args

        director_id = args.get('director_id')
        if director_id is not None:
            movies_query = movies_query.filter(models.Movie.director_id == director_id)

        genre_id = args.get('genre_id')

        if genre_id is not None:
            movies_query = movies_query.filter(models.Movie.genre_id == genre_id)

        movies = movies_query.all()

        return movies_schema.dump(movies), 200

    def post(self):
        """метод для отправки данных"""

        movie = movie_schema.load(request.json)
        db.session.add(models.Movie(**movie))
        db.session.commit()

        return None, 201

@movies_ns.route('/<int:movie_id>/')
class MoviVew(Resource):

    def get(self, movie_id):
        """метод для получения одного фильма"""

        movie = db.session.query(models.Movie).filter(models.Movie.id == movie_id).first()

        if movie is None:
            return 'Не знаю такой фильм', 404

        return movie_schema.dump(movie), 200

    def put(self, movie_id):
        """"метод обновляет данные о конкретном фильме"""

        update_row = db.session.query(models.Movie).filter(models.Movie.id == movie_id).update(request.json)
        if update_row == 0:
            return None, 400

        db.session.commit()
        return None, 204

    def delete(self, movie_id):
        """метод удаляет из базы конкретный фильм"""

        delete_row = db.session.query(models.Movie).filter(models.Movie.id == movie_id).delete()
        if delete_row == 0:
            return None, 400

        db.session.commit()
        return None, 200

@directors_ns.route('/')
class DirectorsView(Resource):

    def get(self):
        """метод для получения всех режиссеров"""

        directors_query = db.session.query(models.Director).all() #запрос в БД

        return directors_schema.dump(directors_query), 200

@directors_ns.route('/<int:director_id>/')
class DirectorView(Resource):

    def get(self,director_id):
        """метод для получения одного режиссера"""

        director = db.session.query(models.Director).filter(models.Director.id == director_id).first()

        if director is None:
            return 'Не знаю такого режиссера', 404

        return director_schema.dump(director), 200

@genre_ns.route('/')
class GenresView(Resource):

    def get(self):
        """метод для получения всех жанров"""

        genres_query = db.session.query(models.Genre).all()

        return genres_schema.dump(genres_query)

@genre_ns.route('/<int:genre_id>/')
class GenreView(Resource):

    def get(self, genre_id):
        """метод для получения одного жанра"""

        genre = db.session.query(models.Genre).filter(models.Genre.id == genre_id).first()

        if genre is None:
            return 'Не знаю такой жанр', 404

        return genre_schema.dump(genre), 200