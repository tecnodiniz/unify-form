import os
import datetime
from flask import Flask
from app.config import Config
from app.main.routes import main_bp

def create_app():
    os.makedirs(Config.UPLOAD_FOLDER, exist_ok=True)
    os.makedirs(Config.FORMS_FOLDER, exist_ok=True)

    app = Flask(__name__, static_folder='static', template_folder='templates')

    app.config.from_object(Config)
    app.jinja_env.globals.update(now=lambda: datetime.now())

    app.register_blueprint(main_bp)



    return(app)
