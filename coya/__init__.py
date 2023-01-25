from flask import Flask
from flask_redis import Redis
from flask_socketio import SocketIO
from config import Config

db = Redis()
socketio = SocketIO()


def create_app(app_config=Config):
    app = Flask(__name__)
    app.config.from_object(app_config)
    db.init_app(app)
    socketio.init_app(app)
    return app
