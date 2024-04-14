from flask import Blueprint
from flask_restful import Api
from app.api.routes.fetch import FetchAll, FetchOne
from app.api.routes.save import Save
from app.api.routes.delete import Delete

# * Create the API V1 blueprint
v1_blueprint = Blueprint("v1", __name__)

# * Generate a Flask API from the blueprint
v1_api = Api(v1_blueprint)

# * Define API Routes
v1_api.add_resource(FetchAll, "/<string:database>/<string:collection>/fetch/all")
v1_api.add_resource(FetchOne, "/<string:database>/<string:collection>/fetch/one")
v1_api.add_resource(Save, "/<string:database>/<string:collection>/save")
v1_api.add_resource(Delete, "/<string:database>/<string:collection>/delete")
