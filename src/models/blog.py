from datetime import datetime
from src import db
from slugify import slugify
import os
from werkzeug.datastructures import FileStorage


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    photo = db.Column(db.String(255))
    description = db.Column(db.Text)
    slug = db.Column(db.String(255), unique=True)
    posts = db.relationship('Post', backref='category', lazy=True)


    def __init__(self, *args, **kwargs):
        if not 'slug' in kwargs:
            kwargs['slug'] = slugify(kwargs.get('name', ''))
        super().__init__(*args, **kwargs)

    def set_photo(self, file: FileStorage):
        ext = file.filename.rsplit('.')[-1]
        name = f"{self.slug}.{ext}"
        name = os.path.join("src", "uploads", "category", name)
        file.save(name)
        self.photo = f"category/{self.slug}.{ext}"

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'slug': self.slug,
            'photo': self.photo,
            'description': self.description,
            'posts': [post.format() for post in self.posts]
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    content = db.Column(db.Text)
    photo = db.Column(db.String(255))
    category_id = db.Column(db.Integer, db.ForeignKey(
        'category.id', ondelete="CASCADE"))

    slug = db.Column(db.String(255), unique=True)
    date = db.Column(db.DateTime,
                             default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        if not 'slug' in kwargs:
            kwargs['slug'] = slugify(kwargs.get('title', ''))
        super().__init__(*args, **kwargs)

    def set_photo(self, file: FileStorage):
        ext = file.filename.rsplit('.')[-1]
        name = f"{self.slug}.{ext}"
        name = os.path.join("src", "uploads", "post", name)
        file.save(name)
        self.photo = f"post/{self.slug}.{ext}"

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'date': self.date,
            'photo': self.photo,
            'slug': self.slug,
            'category_id': self.category_id
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
