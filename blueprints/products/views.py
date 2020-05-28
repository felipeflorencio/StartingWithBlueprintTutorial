from flask import Blueprint

product = Blueprint('product', __name__)


@product.route("/listOfClothes")
def list_of_clothes():
    return "List of clothes"


@product.route("/listOfShoes")
def list_of_shoes():
    return "List of shoes"


@product.route("/listOfTshirts")
def list_of_tshirts():
    return "List of t-shirts"