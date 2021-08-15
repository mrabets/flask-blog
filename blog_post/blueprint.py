from flask import Blueprint, render_template, request


blog_post = Blueprint('blog_post', __name__, url_prefix='/post')

@blog_post.route('/add', methods=('GET', 'POST'))
def add():
    if request.method == 'POST':
        title = request.form['title']
        subtitle = request.form['subtitle']
        author = request.form['author']
        content = request.form['content']

        return f"<h1>{title}<br>{subtitle}<br>{author}<br>{content}</h1>"

    return render_template('add.html')