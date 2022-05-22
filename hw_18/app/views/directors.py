from flask_restx import Resource, Namespace

from..setup_db import db
from ..models import DirectorSchema, Director

director_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)

@director_ns.route('/')
class DirectorView(Resource):
    def get(self):
        all_directors = db.session.query(Director).all()
        return directors_schema.dump(all_directors), 200

@director_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did: int):
        director = Director.query.get(did)
        if director:
            return director_schema.dump(director), 200
        return f'Режисёра с таким id нет',404
