from flask import Flask, jsonify, request, make_response
from data_layer.db_loader import pgstorage

from data_layer.db_loader import VectorDbLoaderFabric as vs_fabric

import logging
app = Flask(__name__)

@app.route('/gapinfo', methods=['GET'])
def there_is_docs():
    print('hello')
    return jsonify('Place for future docs')

@app.route('/vec_storage_action', methods=['POST'])
def make_request_2vec_storage():
    input = request.get_json()
    req = vs_fabric().loader()
    req.request = input['request']

    try:
        req.make_request()
       

    except Exception as ex:
        print(ex)
        raise
        
    return jsonify(200, 'ok')
        

    
