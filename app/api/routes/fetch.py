from math import ceil
from flask_restful import Resource, request, marshal_with
from app.api.models.mongo import Mongo
from app.api.models.auth import require_credentials
from pymongo.errors import OperationFailure


class FetchAll(Resource):
    # Define a PER_PAGE total
    PER_PAGE = 10

    @require_credentials
    def get(self, database: str, collection: str):
        try:
            # Get the arguments passed
            args = request.json

            # Retrieve the args
            username = args["username"]
            password = args["password"]
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

            return {
                "data": list(data),
                "page": page,
                "total_pages": total_pages,
                "total_documents": total_documents,
                "success": True,
            }, 200

        except OperationFailure as of:
            if of.code == 18:
                return {"message": "Authentication failed.", "success": False}, 401
            else:
                return {
                    "message": f"An error occurred: {of}",
                    "success": False,
                }, 500
        except Exception as e:
            return {"message": f"An error occurred: {e}", "success": False}, 500


class FetchOne(Resource):
    def get(self, database: str, collection: str):
        try:
            # Get the arguments passed
            args = request.json

            # Retrieve the args
            username = args["username"]
            password = args["password"]
            query_filter = args["query"] if "query" in args else {}

            # Create the mongodb class
            mongo = Mongo(
                username=username,
                password=password,
                database=database,
                collection=collection,
            )

            # Retrieve the data
            data = mongo.collection.find(query_filter, {"_id": 0}).limit(1)

            if len(data) < 1:
                raise OperationFailure("No data found for this filter")

            return {
                "data": data[0],
                "success": True,
            }, 200

        except OperationFailure as of:
            if of.code == 18:
                return {"message": "Authentication failed.", "success": False}, 401
            else:
                return {
                    "message": f"An error occurred: {of}",
                    "success": False,
                }, 500
        except Exception as e:
            return {"message": f"An error occurred: {e}", "success": False}, 500
