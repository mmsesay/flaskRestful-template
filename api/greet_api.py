'''
This file is responsible for exposing the api
'''
from flask_restful import Resource


class GreetHello(Resource):
    def get(self):
        return {'Greet': '"Hello, World!"'}, 200


class GreetBye(Resource):
    def get(self, name):
        return {'Greet': '"Bye {}"'.format(name)}, 200
