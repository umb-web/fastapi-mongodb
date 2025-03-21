from pymongo import MongoClient


class Database:
    def __init__(self):
        self.client = MongoClient(
            "mongodb+srv://root:root@cluster-1-web.x4qmo.mongodb.net/?retryWrites=true&w=majority&appName=cluster-1-web",
            tlsAllowInvalidCertificates=True,
        )
        self.db = self.client["pruebas"]

    def get_collection(self, collection_name):
        return self.db[collection_name]


database = Database()
