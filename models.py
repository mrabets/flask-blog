from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    subtitle = db.Column(db.String(100))
    author = db.Column(db.String(20))
    date_posted = db.Column(db.DateTime(), default=datetime.now())
    content = db.Column(db.Text)
    