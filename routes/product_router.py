from fastapi import APIRouter, HTTPException, status
from services.product_service import get_products, get_product_by_id

product_rt = APIRouter()


@product_rt.get("/products")
def get_products_endpoint():
    products = get_products()
    return products


@product_rt.get("/product/{id}")
def get_product_id(id: str):
    product = get_product_by_id(id)
    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="product not found"
        )
    return product
