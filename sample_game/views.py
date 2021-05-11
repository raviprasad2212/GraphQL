from flask_restful import Resource, Api
from flask import Flask


app = Flask(__name__)

api = Api(Flask)

class Allgame(Resource):