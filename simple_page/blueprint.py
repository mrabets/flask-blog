from flask import Blueprint, render_template
simple_page = Blueprint('simple_page', __name__)

@simple_page.route('/')
def index():
    return render_template('index.html')

@simple_page.route('/about')
def about():
    return render_template('about.html')

@simple_page.route('/post')
def post():
    return render_template('post.html')

@simple_page.route('/contact')
def contact():
    return render_template('contact.html')