import os
from pymongo import MongoClient


class Mongo:
    def __init__(
        self,
        username: str,
        password: str,
        database: str,
        collection: str,
    ) -> None:
        # Create a mongodb connection
        mongo = MongoClient(
            host=os.environ["DB_HOST"],
            # tls=True,
            # tlsAllowInvalidCertificates=False,
            # tlsCAFile=db_ca_file,
            # tlsCertificateKeyFile=db_cert_file,
            username=username,
            password=password,
        )

        # Retrieve the mbt db
        db = mongo[database]

        # Retrieve the collection openings
        self.collection = db[collection]
