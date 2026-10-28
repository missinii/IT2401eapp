import json
import os
from flask import Flask, render_template, request

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PRODUCTS_PATH = os.path.join(BASE_DIR, 'data', 'products.json')
CATEGORIES_PATH = os.path.join(BASE_DIR, 'data', 'categories.json')


with open(PRODUCTS_PATH, "r", encoding="utf-8") as pf, open(CATEGORIES_PATH, "r", encoding="utf-8") as cf:
    products_data = json.load(pf)
    categories_data = json.load(cf)

@app.context_processor
def common_data():
    return {
        'categories': categories_data
    }

@app.route("/")
@app.route("/products")
def index():

    products = products_data


    kw = request.args.get("kw")
    if kw:
        products = [p for p in products if kw.lower() in p["name"].lower()]


    cate_id = request.args.get("category_id")
    if cate_id:
        products = [p for p in products if int(p["category_id"]) == int(cate_id)]

    return render_template('index.html', products=products)

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/products/<int:product_id>')
def product_detail(product_id):
    product = [p for p in products_data if int(p["id"] == product_id)]
    return render_template('products_detail.html', product = product)
if __name__ == '__main__':
    app.run(debug=True)