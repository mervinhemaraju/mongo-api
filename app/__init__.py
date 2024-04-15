from flask import Flask
from app.api.v1 import v1_blueprint
from app.api.responses.errors import ErrorGeneral as Error
from flask_restful import marshal_with

# from flask_restful import marshal_with

# * Create a Flask Application
app = Flask(__name__)

# * Register API blueprint
app.register_blueprint(v1_blueprint, url_prefix="/api/v1")


#! Error Handlers
@app.errorhandler(404)  #! Handling HTTP 404 NOT FOUND
@marshal_with(Error.error_fields)
def page_not_found(e):
    # * Create a new error object and return it
    return Error(
        message="You've landed on a non-existant page.",
    ), 404


@app.errorhandler(400)  #! Handling HTTP 400 BAD REQUEST
@marshal_with(Error.error_fields)
def page_bad_request(e):
    # * Create a new error object and return it
    return Error(message="You've sent a bad request."), 400
