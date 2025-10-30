import os
import urllib.parse
import pymysql
pymysql.install_as_MySQLdb()

from dotenv import load_dotenv
from flask import Flask
from db_init import db
from my_project.auth.route.airport_route import airport_bp
from my_project.auth.route.plane_route import plane_bp
from my_project.auth.route.flight_route import flight_bp
from flask import Flask, jsonify
from flasgger import Swagger
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    # Зчитуємо правильні дані з .env
    env_user = os.environ.get('API_USER')
    env_pass = os.environ.get('API_PASSWORD')
    
    # Перевіряємо, чи збігаються дані
    if username == env_user and password == env_pass:
        return username  # Успіх!
    return None  # Помилка автентифікації

load_dotenv()

db_user = os.environ.get('DB_USER')
db_pass_raw = os.environ.get('DB_PASSWORD')
db_pass_safe = urllib.parse.quote_plus(db_pass_raw)
db_host = os.environ.get('DB_HOST')
db_name = os.environ.get('DB_NAME')

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{db_user}:{db_pass_safe}@{db_host}:3306/{db_name}"

db.init_app(app)

airport_bp.before_request(auth.login_required)
app.register_blueprint(airport_bp, url_prefix='/api')

plane_bp.before_request(auth.login_required)
app.register_blueprint(plane_bp, url_prefix='/api')

flight_bp.before_request(auth.login_required)
app.register_blueprint(flight_bp, url_prefix='/api')


@app.route('/api/health', methods=['GET'])
def health_check():
    """
    Health check
    ---
    tags:
      - Health
    responses:
      200:
        description: OK
        schema:
          type: object
          properties:
            status:
              type: string
              example: healthy
    """
    return jsonify({"status": "healthy"})


swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": "apispec_1",
            "route": "/apispec_1.json",
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/apidocs",
    
    # Блок для кнопки "Authorize"
    "securityDefinitions": {
        "basicAuth": {
            "type": "basic"
        }
    }
}

Swagger(app, config=swagger_config)



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)