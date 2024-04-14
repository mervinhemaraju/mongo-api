from flask_restful import Resource, request, marshal_with
from app.api.models.auth import require_credentials
from app.api.models.mongo import Mongo


class Delete(Resource):
    @require_credentials
    def get(self, database: str, collection: str):
        return {"message": "GET request not allowed on this route."}, 405

    @require_credentials
    def post(self, database: str, collection: str):
        try:
            # Get the arguments passed
            args = request.json

            # Retrieve the args
            username = args["username"]
            password = args["password"]
            query_filter = args.get("query_filter", {})

            # Create the mongodb class
            mongo = Mongo(
                username=username,
                password=password,
                database=database,
                collection=collection,
            )

            # Delete documents
            result = mongo.collection.delete_many(query_filter)

            return {
                "message": "Documents deleted successfully.",
                "count": result.deleted_count,
                "success": True,
            }, 200

        except Exception as e:
            return {"message": str(e), "success": False}, 500
