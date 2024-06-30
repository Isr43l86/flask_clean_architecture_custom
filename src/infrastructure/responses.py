from flask import jsonify


def create_response(query_result, status_code=200):
    result_dict = query_result.__dict__.copy()
    result_dict.pop('_sa_instance_state', None)

    return jsonify(result_dict), status_code
