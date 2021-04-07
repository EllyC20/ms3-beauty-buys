import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
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
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Check if username exists in the db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username Already Exists, Please Try Again.")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # Put the new user into a session cookie
        session["user"] = request.form.get("username").lower()
        flash("Your Registration Was Successful!")
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Check if username exists in the db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # Ensure password match
            if check_password_hash(
               existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
            else:
                # Wrong password
                flash("Incorrect Username And/Or Password")
                return redirect(url_for("login"))

        else:
            # Username doesn't exist
            flash("Incorrect Username And/Or Password")
            return redirect(url_for("login"))
    return render_template("login.html")


@app.route("/logout")
def logout():
    flash("You Have Signed Out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/new_review", methods=["GET", "POST"])
def new_review():
    if request.method == "POST":
        review = {
            "category_name": request.form.get("category_name"),
            "product_name": request.form.get("product_name"),
            "product_desc": request.form.get("product_desc"),
            "review_detail": request.form.get("review_detail"),
            "url_link": request.form.get("url_link"),
            "created_by": session["user"]
        }
        mongo.db.reviews.insert_one(review)
        flash("Your Review Has Been Added, Thank You.")
        return redirect(url_for("get_reviews"))

    categories = mongo.db.product_category.find().sort("category_name", 1)
    return render_template("new_review.html", categories=categories)


@app.route("/edit_review/<review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "product_name": request.form.get("product_name"),
            "product_desc": request.form.get("product_desc"),
            "review_detail": request.form.get("review_detail"),
            "url_link": request.form.get("url_link"),
            "created_by": session["user"]
        }
        mongo.db.reviews.update({"_id": ObjectId(review_id)}, submit)
        flash("Review Has Been Updated, Thank You.")
        return redirect(url_for("get_reviews"))

    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    categories = mongo.db.product_category.find().sort("category_name", 1)
    return render_template(
        "edit_review.html", review=review, categories=categories)


@app.route("/delete_review/<review_id>")
def delete_review(review_id):
    mongo.db.reviews.remove({"_id": ObjectId(review_id)})
    flash("Your Review Has Been Deleted")
    return redirect(url_for("get_reviews"))


@app.route("/get_reviews")
def get_reviews():
    reviews = mongo.db.reviews.find()
    return render_template("reviews.html", reviews=reviews)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)  # Must be false before submission.
