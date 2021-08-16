from datetime import datetime

from sqlalchemy.orm import backref
from app import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    subtitle = db.Column(db.String(100))
    author = db.Column(db.String(20))
    date_posted = db.Column(db.DateTime(), default=datetime.now())
    content = db.Column(db.Text)
    comments = db.relationship('Comment', backref='post')

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    date_commented = db.Column(db.DateTime(), default=datetime.now())
    comment = db.Column(db.Text)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))

def init_db():
    db.create_all()

if __name__ == '__main__':
    init_db()