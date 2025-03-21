from fastapi import APIRouter
from services.product_service import get_products

product_rt = APIRouter()


@product_rt.get("/products")
def get_products_endpoint():
    products = get_products()
    return products
