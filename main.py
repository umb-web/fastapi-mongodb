from fastapi import FastAPI
from routes.product_router import product_rt

app = FastAPI()

app.include_router(product_rt)
