from math import ceil
from flask_restful import Resource, request
from app.api.models.mongo import Mongo
from app.api.models.auth import require_credentials
from pymongo.errors import OperationFailure
from app.api.responses.errors import ErrorOps as Error
from app.api.responses.fetch_one import FetchOneOutput
from app.api.responses.fetch_all import FetchAllOutput


class FetchAll(Resource):
    # Define a PER_PAGE total
    PER_PAGE = 20

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
            page = args.get("page", 1)
            query_filter = args.get("query", {})

            # Create the mongodb class
            mongo = Mongo(
                username=username,
                password=password,
                database=database,
                collection=collection,
            )

            # Create a page skip
            skip = (page - 1) * self.PER_PAGE

            # Retrieve the data
            data = (
                mongo.collection.find(query_filter, {"_id": 0})
                .skip(skip)
                .limit(self.PER_PAGE)
            )

            # Get the total documents
            total_documents = mongo.collection.count_documents(query_filter)

            # Get the total pages
            total_pages = ceil(total_documents / self.PER_PAGE)

            # Create a new response and return it
            return FetchAllOutput(
                data=list(data),
                total_pages=total_pages,
                page=page,
                per_page=self.PER_PAGE,
                total_documents=total_documents,
                success=True,
            ).response(), 200

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


class FetchOne(Resource):
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
            query_filter = args["query"] if "query" in args else {}

            # Create the mongodb class
            mongo = Mongo(
                username=username,
                password=password,
                database=database,
                collection=collection,
            )

            # Retrieve the data
            data = list(mongo.collection.find(query_filter, {"_id": 0}).limit(1))

            # If no data wa found, raise an exception
            if len(data) < 1:
                raise OperationFailure("No data found for this filter")

            # Create a new output and return it
            return FetchOneOutput(
                data=data[0],
                success=True,
            ).response(), 200

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
