from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", title="Index")


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/home")
def home():
    return redirect("/", code="302")


@app.route("/links")
def links():
    return render_template("links.html", title="Links")
