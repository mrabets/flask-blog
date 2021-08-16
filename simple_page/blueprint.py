from flask import Blueprint, render_template
from models import Post, db

simple_page = Blueprint('simple_page', __name__)

@simple_page.route('/')
def index():
    posts = Post.query.order_by(Post.date_posted.desc()).all()

    return render_template('index.html', posts=posts)

@simple_page.route('/about')
def about():
    return render_template('about.html')

@simple_page.route('/contact')
def contact():
    return render_template('contact.html')