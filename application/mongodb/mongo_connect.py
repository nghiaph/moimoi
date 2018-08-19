from flask_pymongo import PyMongo
from application import app
from application.pref.pref_vars import mongodb

# Initiating variable for MongoDB
app.config["MONGO_URI"] = "mongodb://localhost:27017/" + mongodb
mongo = PyMongo(app)
