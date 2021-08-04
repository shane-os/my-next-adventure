import os
from flask import Flask, render_template
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("pages/home.html", title="My Next Adventure")


@app.route("/attractions")
def attractions():
    return render_template("pages/attractions.html", title="Attractions")


@app.route("/account")
def account():
    return render_template("pages/account.html", title="My Account")


@app.route("/login")
def login():
    return render_template("pages/auth.html", title="Authorization", login=True)


@app.route("/register")
def register():
    return render_template("pages/auth.html", title="Authorization")


@app.route("/contactus")
def contactus():
    return render_template("pages/contactus.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "8080")),
        debug=True)
