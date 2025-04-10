import os
import json
from app import Config

def load_data():
    if os.path.exists(Config.DATA_FILE):
        with open(Config.DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {"produtos": [], "formularios": []}

def save_data(data):
    with open(Config.DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
