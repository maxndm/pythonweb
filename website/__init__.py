from flask import Flask
import mysql.connector
from os import path
from flask_login import LoginManager

#[SQLAlchemy]
from flask_sqlalchemy import SQLAlchemy



#[SQLAlchemy]
#SQLAlchemy object creation
db = SQLAlchemy()
DB_NAME = "data"
DB_USERNAME = "root"
DB_PASSWORD = "root"
DB_ADDRESS = "localhost"

def create_app():
    #Flask initialization
    app = Flask(__name__)
    #Encrypts session data and cookies - ITS SECRET DONT SHOW
    app.config['SECRET_KEY'] = 'RANDOM STRING'

    #[SQLAlchemy]
    #SQLAlchemy initialization - at start there was mysql - changed to mysql+pymysql
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_ADDRESS}/{DB_NAME}'
    db.init_app(app)

    #imports views variable from views.py - need to tell the flask that I have some Blueprints
    from .views import views
    from .auth import auth

    #register Blueprints
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    #[SQLAlchemy]
    #This needs to be imported, so it defines classes which are going to be used in database, before app creates the database
    #Also important for LoginManager
    from .models import User

    create_database()

    #[LoginManager]
    login_manager = LoginManager()
    #where should flask redirect when user is not logged in
    login_manager.login_view = 'views.home'
    #tells the manager what variable represents the app
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))


    return app



def create_database():
    try:
        db = mysql.connector.connect(
            host=DB_ADDRESS,
            user=DB_USERNAME,
            passwd=DB_PASSWORD,
            )

        cursor = db.cursor()
        cursor.execute("show databases;")
        databases = []
        for record in cursor.fetchall():
            databases += record

        if "data" in databases:
            print("\nDatabase already exists\n")
        else:
            cursor.execute('''
            CREATE DATABASE data;
            USE data;

            CREATE TABLE user(
            id INT PRIMARY KEY AUTO_INCREMENT,
            username VARCHAR(20) UNIQUE,
            email VARCHAR(60) UNIQUE,
            password VARCHAR(200),
            name VARCHAR(50),
            surname VARCHAR(50),
            photoname VARCHAR(100)
            );
            '''
            )
            cursor.close()
            print("\nDATABASE created\n")
    except mysql.connector.Error as error:
        print("\nSomething went wrong {}\n".format(error))
