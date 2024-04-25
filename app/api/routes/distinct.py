from flask_restful import Resource, request
from app.api.models.mongo import Mongo
from app.api.models.auth import require_credentials
from pymongo.errors import OperationFailure
from app.api.responses.errors import ErrorOps as Error
from app.api.responses.distinct import Distinct as DistinctOutput


class Distinct(Resource):
    @require_credentials
    def get(self, **kwargs):
        try:
            # Get the arguments passed
            args = request.json

            # Retrieve the kwargs
            database = kwargs["database"]
            collection = kwargs["collection"]
            username = kwargs["username"]
            password = kwargs["password"]

            # Retrieve the args
            field = args.get("field", None)

            # If field is not provided, return an error
            if not field:
                raise Exception("Field is required.")

            # Create the mongodb class
            mongo = Mongo(
                username=username,
                password=password,
                database=database,
                collection=collection,
            )

            # Retrieve the data
            data = mongo.collection.distinct(field)

            # Create a new response output and return it
            return DistinctOutput(message="", data=data).response()

        except OperationFailure as of:
            if of.code == 18:
                # Create a new error response and return it
                return Error(
                    message="Authentication failed.",
                ).response(), 401
            else:
                # Create a new error response and return it
                return Error(
                    message=f"An error occurred: {of}",
                ).response(), 500
        except Exception as e:
            # Create a new error response and return it
            return Error(
                message=f"An error occurred: {e}",
            ).response(), 500
