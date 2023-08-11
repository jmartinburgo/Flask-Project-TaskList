from flask import Flask
from flask_pymongo import PyMongo #No funciono
import pymongo

app=Flask(__name__)

app.config["SECRET_KEY"]="06ae9ca3618ca61eb86c82898660953441b600c1"
#app.config["MONGO_URI"]="mongodb+srv://jmartinburgo19:jmartinburgo19@cluster0.qff17mp.mongodb.net/?retryWrites=true&w=majority"

#set up mongodb
#mongodb_client = PyMongo(app) #No funciono
#db =mongodb_client.db #No funciono



conn = "mongodb+srv://jmartinburgo19:jmartinburgo19@cluster0.qff17mp.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(conn, serverSelectionTimeoutMS=5000)
db = client.db


from application import routes