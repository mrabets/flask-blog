from flask import Blueprint, render_template, request, url_for, redirect
from werkzeug.utils import redirect
from models import Post


blog_post = Blueprint('blog_post', __name__, url_prefix='/post')

@blog_post.route('/add', methods=('GET', 'POST'))
def add():
    if request.method == 'POST':
        title = request.form['title']
        subtitle = request.form['subtitle']
        author = request.form['author']
        content = request.form['content']

        post = Post(title=title, subtitle=subtitle, author=author, content=content)
        
        db.session.add(post)
        db.session.commit()

        return redirect(url_for('simple_page.index'))

    return render_template('add.html')