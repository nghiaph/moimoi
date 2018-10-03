"""
This script runs the provisionWebapp application using a development server.
"""

from os import environ
from application import app
from application.pref.pref_static_vars import HOST, PORT

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', HOST)
    try:
        PORT = int(environ.get('SERVER_PORT', PORT))
    except ValueError:
        PORT = 5000

    app.run(HOST, PORT)
