import json
from json import loads
import os
from flask import Flask, render_template, request
PRODUCTS_PATH = os.path.join("D:/Coding/CNPM/IT2401eapp/", 'data/products.json')
CATEGORIES_PATH = os.path.join("D:/Coding/CNPM/IT2401eapp/", 'data/categories.json')
with open(PRODUCTS_PATH, "r", encoding="utf-8") as pf, open(CATEGORIES_PATH,"r",encoding="utf-8") as cf:
    products_data = json.load(pf)
    categories_data = json.load(cf)
app = Flask(__name__)
@app.route("/")
def index():
    global products_data
    global categories_data
    kw = request.args.get("kw")
    if kw:
        products_data = [p for p in products_data if p["name"].find(kw) >= 0]

    cate_id = request.args.get("category_id")
    if cate_id:
        products_data = [p for p in products_data if p["category_id"] == int(cate_id)]

    return render_template('index.html', categories=categories_data, products=products_data)

@app.route('/products')
def listAll():
    return render_template('index.html', categories=categories_data, products = products_data)
@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/login')
def login():
    return render_template('login.html')



if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)
