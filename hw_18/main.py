from flask import Flask
from flask_restx import Api

from app.config import Config
# from app.models import Movie
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


# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    #create_data(app, db)


# функция
# def create_data(app, db):
#     with app.app_context():
#         db.create_all()
#
#         создать несколько сущностей чтобы добавить их в БД
#
#         with db.session.begin():
#             db.session.add_all(здесь список созданных объектов)
#
#
# app = create_app(Config())
# app.debug = True

if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)

    app.run()