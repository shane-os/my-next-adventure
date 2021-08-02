import os
from flask import Flask, render_template
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)