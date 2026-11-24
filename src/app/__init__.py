from flask import Flask
from sqlalchemy import URL
from flask_sqlalchemy import SQLAlchemy
from configuration.DatabaseConfig import DatabaseConfig
from controller import ClubController
from entity.BaseEntity import BaseEntity
from repository.ClubRepository import ClubRepository


db = SQLAlchemy(model_class=BaseEntity)

URI_CONFIG_KEY = "SQLALCHEMY_DATABASE_URI"
ENGINE_CONFIG_KEY = "SQLALCHEMY_ENGINE_OPTIONS"

def init_app(config: DatabaseConfig):
    app = Flask(__name__)
    # add config
    url = URL.create(
        drivername=config.driver,
        username=config.user,
        password=config.password,
        host=config.host,
        port=config.port,
        database=config.database_name,
    )
    app.config[URI_CONFIG_KEY] = url
    app.config[ENGINE_CONFIG_KEY] = {"pool_pre_ping": True}
    db.init_app(app)

    # Create the repository and pass the scoped session maker
    club_repository = ClubRepository(db.session)
    club_bp = ClubController.create_club_controller_bp(club_repository)
    app.register_blueprint(club_bp)


    app.run(debug=True)
