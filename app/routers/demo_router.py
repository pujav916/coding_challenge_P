from flask import Blueprint, jsonify, request

demo_bp = Blueprint('demo', __name__)

@demo_bp.route('/demo/200', methods=['GET'])
def success():
    """Demo endpoint that always returns 200 OK"""
    return jsonify({
        "status": "success",
        "message": "This is a successful 200 OK response"
    })

@demo_bp.route('/demo/400', methods=['GET'])
def bad_request():
    """Demo endpoint that always returns 400 Bad Request"""
    return jsonify({
        "status": "error",
        "message": "This is a 400 Bad Request response",
        "details": "The request was malformed or missing required parameters"
    }), 400

@demo_bp.route('/demo/404', methods=['GET'])
def not_found():
    """Demo endpoint that always returns 404 Not Found"""
    return jsonify({
        "status": "error",
        "message": "This is a 404 Not Found response",
        "details": "The requested resource does not exist"
    }), 404

@demo_bp.route('/demo/500', methods=['GET'])
def server_error():
    """Demo endpoint that always returns 500 Internal Server Error"""
    return jsonify({
        "status": "error",
        "message": "This is a 500 Internal Server Error response",
        "details": "Something went wrong on the server"
    }), 500
