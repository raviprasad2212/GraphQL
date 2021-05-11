from flask.json import jsonify
from flask_restful import Resource, reqparse
from sqlalchemy import sql
import sqlalchemy
from sqlalchemy.sql.expression import table

from model import UserModel, db, meta

class UserRegistration(Resource):
    def post(self):
        return {'message': 'User registration'}


class UserLogin(Resource):
    def post(self):
        return {'message': 'User login'}
      
      
class UserLogoutAccess(Resource):
    def post(self):
        return {'message': 'User logout'}
      
      
class UserLogoutRefresh(Resource):
    def post(self):
        return {'message': 'User logout'}
      
      
class TokenRefresh(Resource):
    def post(self):
        return {'message': 'Token refresh'}
      
      
class AllUsers(Resource):
    def get(self):
        return {'message': 'List of users'}

    def delete(self):
        return {'message': 'Delete all users'}
      
      
class SecretResource(Resource):
    def get(self):
        return {
            'answer': 42
        }









class UserRegistration(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', help = 'This field cannot be blank', required = True)
        parser.add_argument('password', help = 'This field cannot be blank', required = True)
        parser.add_argument('repassword', help = 'This field cannot be blank', required = True)

        data = parser.parse_args()
        username = data.username
        password = data.password
        repassword = data.repassword
        with db.connect() as conn:
            try:
                if (password == repassword):
                    insert_statement = UserModel.insert().values(username = username, password = password)
                    conn.execute(insert_statement)
                    return jsonify({'succeed': 'Successfully created user {}'.format(username)})
                else:
                    return jsonify({'succeed': False, 'msg': 'The user entered password doe not matches'})
            except sqlalchemy.exc.DatabaseError as e:
                print(e)



class UserLogin(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', help = 'This field cannot be blank', required = True)
        parser.add_argument('password', help = 'This field cannot be blank', required = True)
        data = parser.parse_args()
        return data
