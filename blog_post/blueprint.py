from flask import Blueprint, render_template, request, url_for, redirect
from werkzeug.utils import redirect
from models import Post, Comment, db


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

@blog_post.route('/<int:post_id>')
def post(post_id):
    post = Post.query.filter_by(id=post_id).one()
    comments = Comment.query.filter_by(post_id=post_id).all()

    return render_template('post.html', post=post, comments=comments)

@blog_post.route('/<int:post_id>/edit', methods=('GET', 'POST'))
def edit(post_id):
    post = Post.query.filter_by(id=post_id).one()
    
    if request.method == 'POST':
        post.title = request.form['title']
        post.subtitle = request.form['subtitle']
        post.author = request.form['author']
        post.content = request.form['content']
        
        db.session.commit()

        return redirect(url_for('simple_page.index'))

    return render_template('edit.html', post=post)

@blog_post.route('/<int:post_id>/delete', methods=('POST',))
def delete(post_id):
    Post.query.filter_by(id=post_id).delete()
    db.session.commit()
    
    return redirect(url_for('simple_page.index'))

@blog_post.route('/<int:post_id>/add_comment', methods=('POST',))
def add_comment(post_id):
    username = request.form['username']
    comment = request.form['comment']

    comment = Comment(username=username, comment=comment, post_id=post_id)
    
    db.session.add(comment)
    db.session.commit()

    return redirect(url_for('blog_post.post', post_id=post_id))