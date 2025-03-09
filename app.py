from flask import Flask, jsonify, request, make_response

app = Flask(__name__)

@app.route('/first', methods=['GET'])
def first():
    response = make_response(jsonify({'message': 'Success'}), 200)
    response.headers['Content-Type'] = 'application/json'
    response.headers['Authorization'] = 'Bearer token123'
    return response

@app.route('/second', methods=['GET'])
def second():
    response = make_response(jsonify({'param1': 'value1', 'param2': 'value2'}), 400)
    response.headers['Content-Type'] = 'application/json'
    response.headers['Authorization'] = 'Bearer token123'
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
