from flask import Blueprint, redirect, render_template, request, jsonify, url_for, flash

from src.models.blog import Category, Post
from src.forms.blog import CategoryForm, PostForm
from werkzeug.utils import secure_filename

from os.path import join

category_bp = Blueprint('category', __name__, url_prefix='/category')
category_api = Blueprint('category_api', __name__, url_prefix='/api/category')

post_bp = Blueprint('post', __name__, url_prefix='/post')
post_api = Blueprint('post_api', __name__, url_prefix='/api/post')


@category_bp.route("/")
def all_category():
    query = Category.query.all()
    categories = [item.format() for item in query]
    return render_template("blog/category/index.html", categories=categories)


@category_bp.route("/<slug>")
def category_detail(slug):
    category = Category.query.filter(Category.slug == slug).first() 
    return render_template("blog/category/category_detail.html", category=category)


@category_bp.route("/create", methods=['GET', 'POST'])
def category_create():
    form = CategoryForm()
    if form.validate_on_submit():
        name = form.name.data
        photo = form.photo.data
        description = form.description.data
        new_category = Category(name=name, description=description)
        new_category.set_photo(photo)
        new_category.save()
        return redirect(url_for('category.all_category'))
    else:
        print(form.errors)
    return render_template("blog/category/create.html", form=form)


@category_bp.route("/edit/<int:id>", methods=['GET', 'POST'])
def category_edit(id):

    cat = Category.query.get_or_404(id)
    if request.method == "GET":
        form = CategoryForm(obj=cat)
        form.photo.data = None
        print(cat.format())
    else:
        form = CategoryForm(request.form)
        form.photo.data = request.files.get('photo')
        print(request.files)
        if form.validate_on_submit():
            cat.name = form.name.data
            cat.name = form.name.data
            cat.photo = form.photo.data
            cat.description = form.description.data
            if form.photo.data:
                cat.set_photo(form.photo.data)
            cat.save()
            return redirect(url_for('category.all_category'))
        else:
            print(form.errors)
    return render_template("blog/category/edit.html", form=form)


@category_bp.route("/delete/<int:id>")
def category_delete(id):
    cat = Category.query.get_or_404(id)
    cat.delete()
    flash(f"{cat.name} o`chirildi")
    return redirect(url_for('category.all_category'))


@post_bp.route("/<slug>")
def post_detail(slug):
    post = Post.query.filter(Post.slug == slug).first()
    posts = [item.format()
             for item in Post.query.order_by(Post.date.asc()).all()]
    all_posts = []
    for p in posts:
        all_posts.append({'title': p['title'], 'slug': p['slug']})

    current_post = {'title': post.title, 'slug': post.slug}
    p = all_posts.index(current_post)
    # back = all_posts[current_post-1]
    # next = all_posts[current_post+1]

    return render_template("pages/post_detail.html", post=post)


# @post_bp.route("/create", methods=['GET', 'POST'])
# def post_create():
#     form = PostForm()
#     form.category.choices = [(str(category.id), category.name)
#                              for category in Category.query.all()]
#     if form.validate_on_submit():
#         title = form.title.data
#         content = form.content.data
#         category_id = form.category.data
#         photo = form.photo.data
#         new_post = Post(title=title, content=content, category_id=category_id)
#         new_post.set_photo(photo)
#         new_post.save()
#         return redirect(url_for('index.home'))
#     else:
#         print(form.errors)
#     return render_template("blog/create.html", form=form)
