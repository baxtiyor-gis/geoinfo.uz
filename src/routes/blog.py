from flask import Blueprint, redirect, render_template, request, jsonify, url_for, flash

from src.models.blog import Category, Post
from src.forms.blog import CategoryForm, PostForm
from werkzeug.utils import secure_filename

from os.path import join

category_bp = Blueprint('category', __name__, url_prefix='/category')

post_bp = Blueprint('post', __name__, url_prefix='/post')



@category_bp.route("/")
def all_category():
    query = Category.query.all()
    categories = [item.format() for item in query]
    return render_template("blog/all_category.html", categories=categories)


@category_bp.route("/<slug>")
def category_detail(slug):
    category = Category.query.filter(Category.slug == slug).first() 
    return render_template("blog/category_detail.html", category=category)



@post_bp.route("/")
def all_post(slug):
    posts = Post.query.order_by(Post.date.desc()).all()
    return render_template("blog/all_post.html", posts = posts)


@post_bp.route("/<slug>")
def post_detail(slug):
    post = Post.query.filter(Post.slug == slug).first()
    posts = [item.format()
             for item in Post.query.order_by(Post.date.asc()).all()]
    return render_template("blog/post_detail.html", post=post)




