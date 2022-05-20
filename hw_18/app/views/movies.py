from flask import request
from flask_restx import Resource, Namespace

from..setup_db import db
from..models import MovieSchema, Movie

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

@movie_ns.route('/')
class MovieView(Resource):
    def get(self):
        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')
        year = request.args.get('year')

        movies = Movie.query

        if director_id:
            movies = movies.filter(Movie.director_id == director_id)
        if genre_id:
            movies = movies.filter(Movie.genre_id == genre_id)
        if year:
            movies = movies.filter(Movie.year == year)
        movies = movies.all()
        if not movies:
            return "", 204
        else:
            return movies_schema.dump(movies), 200


    def post(self):
        data = request.get_json()
        new_movies = Movie(**data)
        db.session.add(new_movies)
        db.session.commit
        db.session.close

        return '', 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid: int):
        try:
            movie = db.session.query(Movie).filter(Movie.id == mid).one()
            return movie_schema.dump(movie), 200
        except Exception as e:
            return str(e), 404


    def put(self, mid):
        data = request.get_json()
        movie = Movie.query.get(mid)
        movie.id = data['id']
        movie.title = data['title']
        movie.description = data['description']
        movie.trailer = data['trailer']
        movie.year = data['year']
        movie.rating = data['rating']
        movie.genre_id = data['genre_id']
        movie.director_id = data['director_id']

        db.session.add(movie)
        db.session.commit()
        db.session.close()

        return '', 204


    def delete(self, mid: int):
        movie = Movie.query.get(mid)

        db.session.delete(movie)
        db.session.commit()
        db.session.close()

        return '', 204