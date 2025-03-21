from db.database_conn import database


def get_products():
    collection = database.get_collection("productos")
    products = list(collection.find({}, {"_id": 0}))
    return products
