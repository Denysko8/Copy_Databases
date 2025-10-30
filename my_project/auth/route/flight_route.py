from flask import Blueprint
from my_project.auth.controller.flight_controller import FlightController
from auth_config import auth

flight_bp = Blueprint('flight', __name__)


@flight_bp.route('/flights', methods=['GET'])
@auth.login_required
def get_all_flights():
    """
    Get all flights
    ---
    tags:
      - Flights
    security:
      - basicAuth: []
    responses:
      200:
        description: List of flights
        schema:
          type: array
          items:
            type: object
    """
    return FlightController.get_all_flights()


@flight_bp.route('/flights/<int:flight_id>', methods=['GET'])
@auth.login_required
def get_flight_by_id(flight_id):
    """
    Get flight by id
    ---
    tags:
      - Flights
    security:
      - basicAuth: []
    parameters:
      - name: flight_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Flight found
      404:
        description: Flight not found
    """
    return FlightController.get_flight_by_id(flight_id)


@flight_bp.route('/flights', methods=['POST'])
@auth.login_required
def create_flight():
    """
    Create a new flight
    ---
    tags:
      - Flights
    security:
      - basicAuth: []
    parameters:
      - in: body
        name: body
        description: Note - route_id must reference an existing route in the database
        schema:
          type: object
          properties:
            flight_number:
              type: string
              example: "BA808"
            departure_time:
              type: string
              format: date-time
              example: "2024-12-06T09:00:00"
            arrival_time:
              type: string
              format: date-time
              example: "2024-12-06T13:00:00"
            route_id:
              type: integer
              example: 1
              description: Must be a valid route_id from the route table
        example:
          flight_number: "BA808"
          departure_time: "2024-12-06T09:00:00"
          arrival_time: "2024-12-06T13:00:00"
          route_id: 1
    responses:
      201:
        description: Flight created
      400:
        description: Invalid route_id or bad request
    """
    return FlightController.create_flight()


@flight_bp.route('/flights/<int:flight_id>', methods=['PUT'])
@auth.login_required
def update_flight(flight_id):
    """
    Update flight by id
    ---
    tags:
      - Flights
    security:
      - basicAuth: []
    parameters:
      - name: flight_id
        in: path
        type: integer
        required: true
      - in: body
        name: body
        schema:
          type: object
          properties:
            departure_time:
              type: string
              format: date-time
              example: "2024-12-06T09:00:00"
            arrival_time:
              type: string
              format: date-time
              example: "2024-12-06T13:00:00"
        example:
          departure_time: "2024-12-06T09:00:00"
          arrival_time: "2024-12-06T13:00:00"
    responses:
      200:
        description: Flight updated
      404:
        description: Flight not found
    """
    return FlightController.update_flight(flight_id)


@flight_bp.route('/flights/<int:flight_id>', methods=['DELETE'])
@auth.login_required
def delete_flight(flight_id):
    """
    Delete flight by id
    ---
    tags:
      - Flights
    security:
      - basicAuth: []
    parameters:
      - name: flight_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Flight deleted
      404:
        description: Flight not found
    """
    return FlightController.delete_flight(flight_id)
