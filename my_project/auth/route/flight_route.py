from flask import Blueprint
from my_project.auth.controller.flight_controller import FlightController

flight_bp = Blueprint('flight', __name__)


@flight_bp.route('/flights', methods=['GET'])
def get_all_flights():
    """
    Get all flights
    ---
    tags:
      - Flights
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
def get_flight_by_id(flight_id):
    """
    Get flight by id
    ---
    tags:
      - Flights
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
def create_flight():
    """
    Create a new flight
    ---
    tags:
      - Flights
    parameters:
      - in: body
        name: body
        schema:
          type: object
    responses:
      201:
        description: Flight created
    """
    return FlightController.create_flight()


@flight_bp.route('/flights/<int:flight_id>', methods=['PUT'])
def update_flight(flight_id):
    """
    Update flight by id
    ---
    tags:
      - Flights
    parameters:
      - name: flight_id
        in: path
        type: integer
        required: true
      - in: body
        name: body
        schema:
          type: object
    responses:
      200:
        description: Flight updated
      404:
        description: Flight not found
    """
    return FlightController.update_flight(flight_id)


@flight_bp.route('/flights/<int:flight_id>', methods=['DELETE'])
def delete_flight(flight_id):
    """
    Delete flight by id
    ---
    tags:
      - Flights
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
