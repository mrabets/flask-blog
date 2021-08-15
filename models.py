from datetime import datetime
from app import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    subtitle = db.Column(db.String(100))
    author = db.Column(db.String(20))
    date_posted = db.Column(db.DateTime(), default=datetime.now())
    content = db.Column(db.Text)
    