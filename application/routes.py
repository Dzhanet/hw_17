#хранилище роутов

from flask import current_app as app, request
from flask_restx import Api, Namespace, Resource
from application.models import db
from application import models, schema

api: Api = app.config['api']

movies_ns: Namespace = api.namespace('movies') #создаем неймспейс для фильмов с префиксом movies
movies_schema = schema.Movie(many=True) #может принимать список значений, поэтому True
movie_schema = schema.Movie()

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

@movies_ns.route('/<int:movie_id>/')
class MoviVew(Resource):

    def get(self, movie_id):
        """метод для получения одного фильма"""

        movie = db.session.query(models.Movie).filter(models.Movie.id == movie_id).first()

        if movie is None:
            return 'Не знаю такой фильм', 404

        return movie_schema.dump(movie), 200
