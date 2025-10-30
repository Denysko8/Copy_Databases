from flask import Blueprint
from my_project.auth.controller.plane_controller import PlaneController

plane_bp = Blueprint('plane', __name__)


@plane_bp.route('/planes', methods=['GET'])
def get_all_planes():
    """
    Get all planes
    ---
    tags:
      - Planes
    responses:
      200:
        description: List of planes
        schema:
          type: array
          items:
            type: object
    """
    return PlaneController.get_all_planes()


@plane_bp.route('/planes_with_maintenances', methods=['GET'])
def get_planes_with_maintenances():
    """
    Get planes including their maintenance records
    ---
    tags:
      - Planes
    responses:
      200:
        description: List of planes with maintenance
    """
    return PlaneController.get_planes_with_maintenances()


@plane_bp.route('/planes_with_airline', methods=['GET'])
def get_planes_with_airline():
    """
    Get planes including their airline information
    ---
    tags:
      - Planes
    responses:
      200:
        description: List of planes with airline
    """
    return PlaneController.get_planes_with_airline()


@plane_bp.route('/planes/<int:plane_id>', methods=['GET'])
def get_plane_by_id(plane_id):
    """
    Get plane by id
    ---
    tags:
      - Planes
    parameters:
      - name: plane_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Plane found
      404:
        description: Plane not found
    """
    return PlaneController.get_plane_by_id(plane_id)


@plane_bp.route('/planes', methods=['POST'])
def create_plane():
    """
    Create a new plane
    ---
    tags:
      - Planes
    parameters:
      - in: body
        name: body
        schema:
          type: object
    responses:
      201:
        description: Plane created
    """
    return PlaneController.create_plane()


@plane_bp.route('/planes/<int:plane_id>', methods=['PUT'])
def update_plane(plane_id):
    """
    Update plane by id
    ---
    tags:
      - Planes
    parameters:
      - name: plane_id
        in: path
        type: integer
        required: true
      - in: body
        name: body
        schema:
          type: object
    responses:
      200:
        description: Plane updated
      404:
        description: Plane not found
    """
    return PlaneController.update_plane(plane_id)


@plane_bp.route('/planes/<int:plane_id>', methods=['DELETE'])
def delete_plane(plane_id):
    """
    Delete plane by id
    ---
    tags:
      - Planes
    parameters:
      - name: plane_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Plane deleted
      404:
        description: Plane not found
    """
    return PlaneController.delete_plane(plane_id)
