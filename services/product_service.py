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


def insert_product(product: Product):
    collection = database.get_collection("productos")
    product_dict = product.dict()
    res = collection.insert_one(product_dict)
    return {"id": str(res.inserted_id), "message": "inserted"}


def update_product(id: str, product: Product):
    collection = database.get_collection("productos")
    updated_data = {}

    product_dict = product.dict()

    for k, v in product_dict.items():
        if v is not None:
            updated_data[k] = v

    if not updated_data:
        return {"message": "no data to update"}

    res = collection.update_one({"_id": ObjectId(id)}, {"$set": updated_data})

    if res.matched_count == 0:
        return {"message": "product not found"}

    return {"message": "product updated"}


def delete_product(id: str):
    collection = database.get_collection("productos")

    try:
        result = collection.delete_one({"_id": ObjectId(id)})
        if result.deleted_count == 0:
            return {"message": "product not found"}
    except Exception as e:
        return {"message": f"error: {str(e)}"}

    return {"message": "deleted"}
