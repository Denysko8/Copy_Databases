# app.py
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Container is ALIVE! Problem is in DB connection."

if __name__ == "__main__":
    # Цей блок не виконується в Gunicorn, але корисний для локальних тестів
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))