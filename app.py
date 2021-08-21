# Import packages and environment
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

# App Configuration
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


# Home Page
@app.route("/")
def home():
    return render_template("pages/home.html", title="My Next Adventure")


# Attractions
@app.route("/attractions")
def attractions():
    getattractions = mongo.db.attractions.find()
    return render_template(
        "pages/attractions.html",
        title="Attractions", attractions=getattractions)


# Attraction Search & Retrieval
@app.route("/search", methods=["GET", "POST"])
def search():
    target = request.form.get("target")
    attractions = list(
        mongo.db.attractions.find({"$text": {"$search": target}}))
    return render_template(
        "pages/attractions.html", title="Attractions", attractions=attractions)


# Login Page
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user_exists = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if user_exists:

            if check_password_hash(user_exists["password"], request.form.get("userpassword")):
                session['user'] = request.form.get("username").lower()
                flash("You have Successfully Logged In! Thank You!")
                return redirect(url_for("dashboard", username=session['user']))
            else:
                flash("Incorrect Username/Password. Please try again")
                return redirect(url_for("login"))
        else:
            flash("Username Not Registered. Please create an account!")
            return redirect(url_for("login"))

    return render_template("pages/login.html", title="Login")


# Register
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        user_exists = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if user_exists:
            flash("Username already in use")
            return redirect(url_for("register"))

        if request.form.get("userpassword") != request.form.get("confirmpassword"):
            flash("Passwords do not match!")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(
                request.form.get("userpassword")),
            "admin": False
        }

        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("You have Successfully Registered! Thank You!")
        return redirect(url_for("dashboard", username=session["user"]))

    return render_template("pages/register.html", title="Register")


# Dashboard
@app.route("/dashboard/<username>", methods=["GET", "POST"])
def dashboard(username):
    username = mongo.db.users.find_one(
        {'username': session['user']})['username']
    if session['user']:
        return render_template("pages/dashboard.html", username=username)
    else:
        return redirect(url_for("home"))


# Edit Attraction
@app.route("/edit_attraction/<attraction_id>", methods=["GET", "POST"])
def edit_attraction(attraction_id):
    if request.method == "POST":
        if request.form.get("freeattraction") == "Yes":
            attractionprice = "Yes"
        else:
            attractionprice = "No"
        if request.form.get("bookticket") == "Yes":
            prebook = "Yes"
        else:
            prebook = "No"
        if request.form.get("children") == "Yes":
            child = "Yes"
        else:
            child = "No"
        attraction_edit = {
            "attraction_name": request.form.get("attraction_name"),
            "location": request.form.get("location"),
            "description": request.form.get("description"),
            "image": request.form.get("image"),
            "free": attractionprice,
            "pre_booking_required": prebook,
            "suitable_for_children": child
        }
        mongo.db.attractions.update(
            {"_id": ObjectId(attraction_id)}, attraction_edit)
        flash("Attraction Successfully Updated!")
        return redirect(url_for("attractions"))

    attraction_to_edit = mongo.db.attractions.find_one(
        {"_id": ObjectId(attraction_id)})
    return render_template(
        "pages/edit_attraction.html", attractions=attraction_to_edit)


# Add Attraction
@app.route("/add_attraction", methods=["GET", "POST"])
def add_attraction():
    if request.method == "POST":
        if request.form.get("freeattraction") == "Yes":
            attractionprice = "Yes"
        else:
            attractionprice = "No"
        if request.form.get("bookticket") == "Yes":
            prebook = "Yes"
        else:
            prebook = "No"
        if request.form.get("children") == "Yes":
            child = "Yes"
        else:
            child = "No"
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

    return render_template("pages/add_attraction.html", title="Add Attraction")


# Delete Attraction
@app.route("/delete_attraction/<attraction_id>")
def delete_attraction(attraction_id):
    mongo.db.attractions.remove({"_id": ObjectId(attraction_id)})
    flash("Attraction Deleted Successfully!")
    return redirect(url_for("attractions"))


# Logout
@app.route("/logout")
def logout():
    flash("You have successfully logged out!")
    session.pop("user")
    return redirect(url_for("login"))


# Contact Us
@app.route("/contactus")
def contactus():
    return render_template("pages/contactus.html", title="Contact Us")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=os.environ.get("DEBUG"))
