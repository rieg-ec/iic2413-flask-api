from flask import Flask
from flask_restful import Api
from decouple import config
from api.resources import (
    Messages, Message, TextSearch, Users, User, DeleteMessage
)

app = Flask(__name__)

app.config.update(
    DEBUG=config('DEBUG'),
    ENV=config('ENV')
)

api = Api(app)

api.add_resource(Messages, '/messages')
api.add_resource(Message, '/messages/<int:id>')
api.add_resource(DeleteMessage, '/message/<int:id>')

api.add_resource(Users, '/users')
api.add_resource(User, '/users/<int:id>')

api.add_resource(TextSearch, '/text-search')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
