from flask import jsonify
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'message': 'Hello, World!'})