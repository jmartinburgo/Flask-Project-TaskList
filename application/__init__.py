from flask import Flask
from flask_pymongo import PyMongo

app=Flask(__name__)

app.config["SECRET_KEY"]="06ae9ca3618ca61eb86c82898660953441b600c1"
app.config["MONGO_URI"]="mongodb+srv://jmartinburgo:jmartinburgo@cluster0.qff17mp.mongodb.net/?retryWrites=true&w=majority"

#set up mongodb
mongodb_client = PyMongo(app)
db= mongodb_client.db

from application import routes