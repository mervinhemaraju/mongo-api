from flask_restful import Resource, request, marshal_with
from app.api.models.auth import require_credentials
from app.api.models.mongo import Mongo
from app.api.responses.write_ops import WriteOps
from app.api.responses.errors import ErrorOps as Error


class Delete(Resource):
    @require_credentials
    def get(self, database: str, collection: str):
        return {"message": "GET request not allowed on this route."}, 405

    @require_credentials
    @marshal_with(WriteOps.wo_fields)
    def post(self, database: str, collection: str):
        try:
            # Get the arguments passed
            args = request.json

            # Retrieve the args
            username = args["username"]
            password = args["password"]
            query_filter = args.get("query", {})

            # Create the mongodb class
            mongo = Mongo(
                username=username,
                password=password,
                database=database,
                collection=collection,
            )

            # Delete documents
            result = mongo.collection.delete_many(query_filter)

            # Create a new response and return it
            return WriteOps(
                message="Documents deleted successfully.",
                count=result.deleted_count,
            ), 200

        except Exception as e:
            # Create a new error response and return it
            return Error(str(e)), 500
