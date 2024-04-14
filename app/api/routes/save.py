from flask_restful import Resource, request, marshal_with
from app.api.models.auth import require_credentials
from app.api.models.mongo import Mongo


class Save(Resource):
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
            documents = args.get("documents", None)

            # Verify if document is not empty
            if documents is None:
                raise Exception("No documents provided to save.")

            # Create the mongodb class
            mongo = Mongo(
                username=username,
                password=password,
                database=database,
                collection=collection,
            )

            # Save the documents
            result = mongo.collection.insert_many(documents)

            return {
                "message": "Documents saved successfully.",
                "count": len(result.inserted_ids),
                "success": True,
            }, 200
        except Exception as e:
            return {"message": str(e), "success": False}, 500
