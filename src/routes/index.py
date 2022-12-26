from flask import Blueprint, redirect, render_template, request, jsonify, url_for
from src.models.blog import Post
from src.forms.blog import PostForm
from flask_ckeditor import upload_success, upload_fail

bp = Blueprint('index', __name__, url_prefix='/')



@bp.route("/")
def home():
    posts = Post.query.order_by(Post.date.desc()).all()
    return render_template("pages/home.html", posts = posts)

    




