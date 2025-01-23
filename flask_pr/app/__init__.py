from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Настройки приложения
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
    app.config['SECRET_KEY'] = 'your_secret_key'

    # Инициализация базы данных
    db.init_app(app)

    # Регистрация маршрутов и моделей
    with app.app_context():
        from . import models
        from .routes import bp  # Импортируем Blueprint из routes.py
        db.create_all()  # Создание таблиц в базе данных
        app.register_blueprint(bp)  # Регистрируем маршруты из Blueprint

    return app