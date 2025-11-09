import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    """
    Простий роут, щоб перевірити, чи живий контейнер.
    """
    return "Container is ALIVE! The problem is 100% the DB connection."

@app.route('/api/health', methods=['GET'])
def health_check():
    """
    Health check, який не потребує бази даних.
    """
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    # Gunicorn ігнорує цей блок, але це правильно для Cloud Run
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))