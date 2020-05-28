from flask import Blueprint


contact = Blueprint('contact', __name__)


@contact.route("/contactMe")
def contact_me():
    return "Contact Me"

@contact.route("/contactForSponsor")
def contact_for_sponsor():
    return "Contact for Sponsor"