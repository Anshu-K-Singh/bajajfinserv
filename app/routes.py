from flask import Blueprint, jsonify

bp = Blueprint('main', __name__)

@bp.route('/bfhl', methods=['GET'])
def get_operation_code():
    return jsonify({"operation_code": 1}), 200
