from flask import Flask, request
from flask_restplus import Resource, Api

app = Flask(__name__)
api = Api(app)

# Importing endpoints will add them to api
from endpoints import pets
