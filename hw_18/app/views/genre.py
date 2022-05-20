from flask_restx import Resource, Namespace

from..setup_db import db
from ..models import GenreSchema, Genre

genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)

@genre_ns.route('/')
class GenreView(Resource):
    def get(self):
        all_genres = db.session.query(Genre).all()
        return genres_schema.dump(all_genres), 200

@genre_ns.route('/<int:did>')
class GenreView(Resource):
    def get(self, did: int):
        try:
            genre = db.session.query(Genre).filter(Genre.id == did).one()
            return genre_schema.dump(genre), 200
        except Exception as e:
            return str(e), 404