from flask_restful import Resource, request, marshal_with
from app.api.models.auth import require_credentials
from app.api.models.mongo import Mongo
from app.api.responses.write_ops import WriteOps
from app.api.responses.errors import ErrorOps as Error


class Save(Resource):
    @require_credentials
    @marshal_with(WriteOps.wo_fields)
    def post(self, **kwargs):
        try:
            # Get the arguments passed
            args = request.json

            # Retrieve the kwargs
            database = kwargs["database"]
            collection = kwargs["collection"]
            username = kwargs["username"]
            password = kwargs["password"]

            # Retrieve the args
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

            # Create a new response and return it
            return WriteOps(
                message="Documents saved successfully.", count=len(result.inserted_ids)
            ), 200

        except Exception as e:
            # Create a new error response and return it
            return Error(str(e)), 500
