from flask import request, Blueprint, redirect
from ..models import User

login_blueprint = Blueprint('login', __name__)

@login_blueprint.route("/login", methods=['POST'])
def login():
    username = request.form["username"]
    password = request.form["password"]
    user = User.query.filter_by(username=username).first()
    if user and user.password == password:
        return redirect("http://localhost:3001/blogs") 
    else:
        return redirect("http://localhost:3001/login", 404, "User not found")
