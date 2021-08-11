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


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = mongo.db.users
        user_exists = user.find_one({"username": request.form.get("username").lower()})

        if user_exists:

            if check_password_hash(user_exists["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("You have Successfully Logged In! Thank You!")
                return render_template("pages/dashboard.html", title="Login")
            else:
                flash("Incorrect Username/Password. Please try again")
                return render_template("pages/account.html", title="Login")

        else:
            flash("Username Not Registered. Please create an account!")
            return render_template("pages/account.html", title="Login")

    return render_template("pages/account.html", title="Login")        


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        user = mongo.db.users
        user_exists = user.find_one({"username": request.form.get("username").lower()})

        if user_exists:
            flash("Username already in use")
            return redirect(url_for("register"))

        if request.form.get("userpassword") != request.form.get("confirmpassword"):
            flash("Passwords do not match!")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("userpassword")),
            "admin": False
        }

        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        return redirect(url_for("dashboard"))
        flash("You have Successfully Registered! Thank You!")
    return render_template("pages/auth.html", title="Authorization")


@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if request.method == "POST":
        if request.form.get("freeattraction") == "Yes":
            attractionprice = True
        else:
            attractionprice = False
        if request.form.get("bookticket") == "Yes":
            prebook = True
        else:
            prebook = False
        if request.form.get("children") == "Yes":
            child = True
        else:
            child = False
        newattraction = {
            "attraction_name": request.form.get("attraction_name"),
            "location": request.form.get("location"),
            "description": request.form.get("description"),
            "image": request.form.get("image"),
            "free": attractionprice,
            "pre_booking_required": prebook,
            "suitable_for_children": child
        }
        mongo.db.attractions.insert_one(newattraction)
        flash("New Attraction Added!")
        return redirect(url_for("attractions"))

    return render_template("pages/dashboard.html", title="User Profile")


@app.route("/contactus")
def contactus():
    return render_template("pages/contactus.html", title="Contact Us")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=os.environ.get("DEBUG"))
