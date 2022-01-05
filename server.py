'''
Server.py file is the applcation starter
'''
from app import init_app

server = init_app()

if __name__ == '__main__':
    '''The application engine'''
    server.run(debug=True)
