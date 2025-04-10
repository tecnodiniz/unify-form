import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRETE_KEY = os.environ.get('SECRET_KEY','@@l0ck3d0u7@@')
    OPEN_IA_KEY = os.environ.get('OPENAI_API_KEY','')
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
    FORMS_FOLDER = os.path.join(BASE_DIR, 'forms')
    IMAGE_FOLDER = os.path.join(BASE_DIR, 'img')
    ALLOWED_EXTENSIONS = {'pdf', 'docx', 'doc'}
    DATA_FILE = os.path.join(BASE_DIR,'services', 'data.json')

