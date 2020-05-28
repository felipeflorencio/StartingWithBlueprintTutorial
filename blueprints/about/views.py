from flask import Blueprint


about = Blueprint('about', __name__)


@about.route("/aboutMe")
def about_me():
    return "About me"


@about.route("/aboutMyWork")
def about_my_work():
    return "Abouy my work"