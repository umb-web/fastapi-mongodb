from fastapi import APIRouter, HTTPException, status
from services.product_service import (
    get_products,
    get_product_by_id,
    insert_product,
    update_product,
    delete_product,
)
from models.product_model import Product

product_rt = APIRouter()


@product_rt.get("/products")
def get_products_endpoint():
    products = get_products()
    return products


@product_rt.get("/products/{id}")
def get_product_id(id: str):
    product = get_product_by_id(id)
    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="product not found"
        )
    return product


@product_rt.post("/products")
def post_product(product: Product):
    return insert_product(product)


@product_rt.put("/products/{id}")
def put_product(id: str, product: Product):
    return update_product(id, product)


@product_rt.delete("/products/{id}")
def delete_product_(id: str):
    return delete_product(id)
