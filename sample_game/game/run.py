from flask import Flask
from flask_restful import Api
from flask_graphql import GraphQLView
from graphql_service import schema


app = Flask(__name__)
api = Api(app)

import views, resources

api.add_resource(resources.UserRegistration, '/registration')
api.add_resource(resources.UserLogin, '/login')
api.add_resource(resources.UserLogoutAccess, '/logout/access')
api.add_resource(resources.UserLogoutRefresh, '/logout/refresh')
api.add_resource(resources.TokenRefresh, '/token/refresh')
api.add_resource(resources.AllUsers, '/users')
api.add_resource(resources.SecretResource, '/secret')




# GraphQL Service
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True # for having the GraphiQL interface
    )
)



if __name__ == '__main__':
    app.run(debug=True)