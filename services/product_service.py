from db.database_conn import database
from bson import ObjectId
from models.product_model import Product


def get_products():
    collection = database.get_collection("productos")
    products = list(collection.find({}, {"_id": 0}))
    return products


def get_product_by_id(id: str):
    collection = database.get_collection("productos")
    try:
        ob_id = ObjectId(id)
    except:
        return None

    product = collection.find_one({"_id": ob_id})

    if product:
        return Product(
            name=product["name"],
            description=product["description"],
            price=product["price"],
        )
    return None
