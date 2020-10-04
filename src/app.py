from flask import Flask, jsonify
from flask_restful import Api

from src.apis.api import StudentListAPI, StudentIdAPI, HelloWorld

from src.config import DevelopmentConfig


class Create:
	def __init__(self, app):
		self.app = app

	@classmethod
	def create_app():
		DevelopmentConfig.Config()

	    app = Flask(__name__)
	    app.config.from_object(DevelopmentConfig.URI)

	    api = Api(app)

	    api.add_resource(HelloWorld, '/hello')
	    api.add_resource(StudentListAPI,'/student')
	    api.add_resource(StudentIdAPI,'/student/<index>')

	    return cls(app)






