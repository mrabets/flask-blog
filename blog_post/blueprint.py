from flask import Blueprint, render_template


blog_post = Blueprint('blog_post', __name__, url_prefix='/post')

@blog_post.route('/add')
def add():
    return render_template('add.html')