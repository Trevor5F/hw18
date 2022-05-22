from flask import Flask
from flask_restx import Api

from app.config import Config
from app.setup_db import db
from app.views.movies import movie_ns
from app.views.directors import director_ns
from app.views.genre import genre_ns



def create_app(config: Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config)
    register_extensions(app)
    app.config['RESTX_JSON'] = {'ensure_ascii': False, 'indent': 3}
    return app


def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)



if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)

    app.run()