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

app = Flask(__name__)


load_dotenv()

db_user = os.environ.get('DB_USER')
db_pass_raw = os.environ.get('DB_PASSWORD')
db_pass_safe = urllib.parse.quote_plus(db_pass_raw)
db_host = os.environ.get('DB_HOST')
db_name = os.environ.get('DB_NAME')

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{db_user}:{db_pass_safe}@{db_host}:3306/{db_name}"

db.init_app(app)

app.register_blueprint(airport_bp, url_prefix='/api')
app.register_blueprint(plane_bp, url_prefix='/api')
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


@app.route('/api/airports_direct', methods=['GET'])
def get_all_airports_direct():
    """
    Direct GET all airports (uses AirportController and DB session)
    ---
    tags:
      - Airports
    responses:
      200:
        description: OK
        schema:
          type: array
          items:
            type: object
    """
    # Query the Airport model directly so Swagger shows DB-backed response
    # Local import to avoid circular imports at module load
    from my_project.auth.models.airport import Airport

    airports = db.session.query(Airport).all()
    return jsonify([airport.to_dict() for airport in airports])


@app.route('/api/airports/count', methods=['GET'])
def get_airports_count():
    """
    Get total number of airports
    ---
    tags:
      - Airports
    responses:
      200:
        description: OK
        schema:
          type: object
          properties:
            count:
              type: integer
              example: 5
    """
    from my_project.auth.models.airport import Airport

    total = db.session.query(Airport).count()
    return jsonify({"count": total})


if __name__ == '__main__':
  # Initialize Swagger after all routes and blueprints are registered
  # Use a permissive rule_filter so Flasgger includes blueprint routes as well
  swagger_config = {
      "headers": [],
      "specs": [
          {
              "endpoint": "apispec_1",
              "route": "/apispec_1.json",
              # include all routes
              "rule_filter": lambda rule: True,
              "model_filter": lambda tag: True,
          }
      ],
      "static_url_path": "/flasgger_static",
      "swagger_ui": True,
      "specs_route": "/apidocs"
  }

  Swagger(app, config=swagger_config)

  app.run(host="0.0.0.0", port=5000)