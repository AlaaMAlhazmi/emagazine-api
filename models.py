import os
from sqlalchemy import Column, String, Integer, Date, Text, create_engine
from flask_sqlalchemy import SQLAlchemy
import json

database_name = "e_magazine_db"
database_path = "postgresql://{}:{}@{}/{}".format(
    'postgres', 'postgres', 'localhost:5432', database_name)
db = SQLAlchemy()

'''
setup_db(app)

'''


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


'''
Author Model

'''


class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    gender = db.Column(db.String)
    email = db.Column(db.String(120))
    articles = db.relationship('Article', backref='authors', lazy=True)

    def __init__(self, name, gender, email):
        self.name = name
        self.gender = gender
        self.email = email

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'gender': self.gender,
            'email': self.email
        }


'''
Article Model

'''


class Article(db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    date = db.Column(db.Date)
    category = db.Column(db.String)
    content = db.Column(db.Text)
    author_id = db.Column(
        db.Integer,
        db.ForeignKey('authors.id'),
        nullable=False)

    def __init__(self, title, date, category, content, author_id):
        self.title = title
        self.date = date
        self.category = category
        self.content = content
        self.author_id = author_id

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'date': self.date,
            'category': self.category,
            'content': self.content,
            'author_id': self.author_id
        }
