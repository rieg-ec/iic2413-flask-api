from flask import Flask
from flask_restful import Api

from api.resources import (
    Messages, Message, TextSearch, Users, User
)

app = Flask(__name__)
api = Api(app)

api.add_resource(Messages, '/messages')
api.add_resource(Message, '/messages/<int:id>')

api.add_resource(Users, '/users')
api.add_resource(User, '/users/<int:id>')

api.add_resource(TextSearch, '/text-search')

if __name__ == '__main__':
    app.run(debug=True)
