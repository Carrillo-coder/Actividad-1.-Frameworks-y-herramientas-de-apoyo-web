from flask import Flask, request, jsonify
from flask_cors import CORS
import pymssql

app = Flask(__name__)
CORS(app)

# Database configuration
server = "localhost"
port = 1433
database = "master"
username = "sa"
password = "YourPassword123!"

# Database connection function
def get_connection():
    return pymssql.connect(server=server, port=port, user=username, password=password, database=database)

@app.route('/get', methods=['GET'])
def get():
    return "Hello World", 200

@app.route('/post', methods=['POST'])
def post():
    return "Item creado", 201

@app.route('/put/<int:id>', methods=['PUT'])
def put(id):
    return "Item actualizado: " + str(id), 200

@app.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    return "Item eliminado: " + str(id), 200

if __name__ == '__main__':
    app.run(debug=True, port=2025)
