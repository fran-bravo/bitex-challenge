from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

from src.initializers import registration_parser, registration_service, registration_validator
from src.initializers import identification_parser, identification_service, identification_validator
#from src.initializers import domicile_service


app = Flask(__name__)
CORS(app, support_credentials=True)


@app.route('/user', methods=['POST'])
@cross_origin(supports_credentials=True)
def user_registration():
    try:
        registration_data = registration_parser.parse(request)
        registration_validator.validate(registration_data)

        user, issue, seed = registration_service.create(registration_data)

        response_object = {
            'status': 'success',
            'payload': {
                'user': {
                    'id': user.id
                },
                'issue': {
                    'id': issue.id
                },
                'seed': {
                    'id': seed.id
                }
            }
        }
        return jsonify(response_object)
    except Exception as e:
        return jsonify({'status': 'error'}), 500


@app.route('/user/id', methods=['POST'])
@cross_origin(supports_credentials=True)
def user_identification():
    try:
        identification_data = identification_parser.parse(request)
        identification_validator.validate(identification_data)

        identification_seed, attachments_seeds = identification_service.create(
            identification_data['data'],
            identification_data['files'],
            identification_data['issue']['id']
        )

        response_object = {
            'status': 'success',
            'payload': {
                'identification': {
                    'id': identification_seed.id
                },
                'attachments': [{'id': seed.id for seed in attachments_seeds}]
            }
        }
        return jsonify(response_object)
    except Exception as e:
        return jsonify({'status': 'error'}), 500


@app.route('/domicile', methods=['POST'])
@cross_origin(supports_credentials=True)
def domicile():
    user_data = registration_parser.parse(request)
    registration_validator.validate_domicile(user_data)

    #domicile_service.create(user_data)

    response_object = {'status': 'success', 'payload': user_data}
    return jsonify(response_object)
