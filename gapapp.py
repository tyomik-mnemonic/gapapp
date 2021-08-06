from flask import Flask, jsonify, request, make_response

app = Flask(__name__)

@app.route('/gapinfo', methods=['GET'])
def there_is_docs():
    print('hello')
    return jsonify('Place for future docs')

