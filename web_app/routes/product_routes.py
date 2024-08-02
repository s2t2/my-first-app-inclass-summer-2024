# this is the "web_app/routes/product_routes.py" file...

from flask import Blueprint, render_template

from app.products import get_products

product_routes = Blueprint("product_routes", __name__)

@product_routes.route("/products")
def products():
    print("LIST PRODUCTS...")
    products = get_products()
    return render_template("products.html", products=products)

@product_routes.route("/api/products.json")
def products_api():
    print("LIST PRODUCTS (API)...")
    products = get_products()
    return {"products": products}
