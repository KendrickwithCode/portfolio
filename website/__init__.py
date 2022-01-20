from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
def create_app():
    app = Flask(__name__)
    app.debug = True
    app.secret_key = 'folio'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.sqlite'
    db.init_app(app)

    from . import views
    app.register_blueprint(views.bp)

    from . import about
    app.register_blueprint(about.bp)

    bootstrap = Bootstrap(app)
    return app
