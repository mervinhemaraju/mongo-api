import os
from flask import Flask, redirect, url_for
from app.api.v1 import v1_blueprint

# from flask_restful import marshal_with

# * Create a Flask Application
app = Flask(__name__)

# * Register API blueprint
app.register_blueprint(v1_blueprint, url_prefix="/api/v1")


# # * Redirect to the correct web page by default
# @app.route("/")
# @app.route("/web")
# def page_web():
#     return redirect(url_for("web.home_view"))


# #! Error Handlers
# @app.errorhandler(404)  #! Handling HTTP 404 NOT FOUND
# @marshal_with(Error.error_fields)
# def page_not_found(e):
#     # * Create a new error object and return it
#     return Error(
#         message="You've landed on a non-existant page. Please check our docs at https://github.com/mervinhemaraju/mauritius-emergency-service-api",
#         code=404,
#     ), 404


# @app.errorhandler(400)  #! Handling HTTP 400 BAD REQUEST
# @marshal_with(Error.error_fields)
# def page_bad_request(e):
#     # * Create a new error object and return it
#     return Error(
#         message="You've sent a bad request. Please check our docs at https://github.com/mervinhemaraju/mauritius-emergency-service-api",
#         code=400,
#     ), 400
