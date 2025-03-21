from pydantic import BaseModel
from typing import Optional


class Product(BaseModel):
    name: str
    descripcion: Optional[str] = None
    price: float
