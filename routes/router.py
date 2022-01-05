# router.py

from api.greet_api import GreetHello, GreetBye


def initialize_routes(api):
  api.add_resource(GreetHello, '/api/v1/greetHello')
  api.add_resource(GreetBye, '/api/v1/greetBye/<string:name>')
