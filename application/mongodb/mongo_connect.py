from flask_pymongo import PyMongo
from application import app
from application.pref.pref_static_vars import moimoidb
# Initiating variable for MongoDB

if __name__ == '__main__':
    app.config["MONGO_URI"] = "mongodb://localhost:27017/" + moimoidb
mongo = PyMongo(app)
