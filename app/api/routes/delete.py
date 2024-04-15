from flask_restful import Resource, request, marshal_with
from app.api.models.auth import require_credentials
from app.api.models.mongo import Mongo
from app.api.responses.write_ops import WriteOps
from app.api.responses.errors import ErrorOps as Error


class Delete(Resource):
    @require_credentials
    @marshal_with(WriteOps.wo_fields)
    def delete(self, **kwargs):
        try:
            # Get the arguments passed
            args = request.json

            # Retrieve the kwargs
            database = kwargs["database"]
            collection = kwargs["collection"]
            username = kwargs["username"]
            password = kwargs["password"]

            # Retrieve the args
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
