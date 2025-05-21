from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
import json

app = FastAPI()
templates = Jinja2Templates(directory="templates")

def load_products():
    with open("products.json", "r") as file:
        return json.load(file)


# This will return HTML page products
@app.get("/products", response_class=HTMLResponse)
async def get_all_products(request: Request):
    return templates.TemplateResponse("products.html", {"request": request, "products": load_products()} )


@app.get("/products/category/{category_name}")
def get_products_by_category(category_name: str):
    products = load_products()
    filtered = [p for p in products if p["category_name"].lower() == category_name.lower()]
    print(filtered)
    if not filtered:
        print("not found")
        raise HTTPException(status_code=404, detail="No products found in this category")
    print(f"found {category_name}!")
    return filtered


@app.get("/products/brand/{brand_name}")
def get_products_by_brand(brand_name: str):
    products = load_products()
    filtered = [p for p in products if p["brand_name"].lower() == brand_name.lower()]
    if not filtered:
        raise HTTPException(status_code=404, detail="No products found for this brand")
    return filtered
