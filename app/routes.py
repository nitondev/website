import csv
from flask import Blueprint, render_template, redirect

bp = Blueprint("main", __name__)

# Read the redirects.csv file.
redirects = {}
with open("redirects.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        redirects[row["/path"]] = (int(row["status_code"]), row["target_url"])

@bp.route("/")
def index():
    return render_template("index.j2", page="home")

@bp.route("/posts")
def posts():
    return render_template("posts.j2", page="posts")


@bp.route("/<path:path>")
def handle_redirects(path):
    full_path = "/" + path
    if full_path in redirects:
        status_code, target_url = redirects[full_path]
        return redirect(target_url, code=status_code)
    return render_template("404.j2"), 404

@bp.app_errorhandler(404)
def page_not_found(e):
    return render_template("404.j2"), 404
