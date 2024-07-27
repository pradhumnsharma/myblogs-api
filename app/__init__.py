from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/myblogs'
    db.init_app(app)
    migrate.init_app(app, db)
    print("GETTING EHRE")
    with app.app_context():
        # Import routes and models within the application context
        from .models import (Blog, User)  # Ensure models are imported
        # db.create_all()  # Uncomment this for initial development  

    return app