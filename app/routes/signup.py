from flask import request, Blueprint, redirect
from ..models import User
from .. import db

signup_blueprint = Blueprint('signup', __name__)

@signup_blueprint.route("/signup", methods=['POST'])
def signup():
    first_name = request.form["firstname"]
    last_name = request.form["lastname"]
    email = request.form["email"]
    username = request.form["username"]
    password = request.form["password"]
    user = User(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
    db.session.add(user)
    db.session.commit()

    return redirect("http://localhost:3001/blogs") 