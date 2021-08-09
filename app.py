import os
from flask import (
    Flask, render_template,
    flash, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")
def home():
    return render_template("pages/home.html", title="My Next Adventure")


@app.route("/attractions")
def attractions():
    getattractions = mongo.db.attractions.find()
    return render_template(
        "pages/attractions.html",
        title="Attractions", attractions=getattractions)


@app.route("/account")
def account():
    return render_template("pages/account.html", title="My Account")


@app.route("/login")
def login():
    return render_template(
        "pages/auth.html",
        title="Authorization",
        login=True)


@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("pages/auth.html", title="Authorization")


@app.route("/contactus")
def contactus():
    return render_template("pages/contactus.html", title="Contact Us")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
