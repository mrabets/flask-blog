from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from simple_page.blueprint import simple_page

app = Flask(__name__)
app.register_blueprint(simple_page)

if app.config["ENV"] == "production":
    app.config.from_object("config.ProductionConfig")
else:
    app.config.from_object("config.DevelopmentConfig")

db = SQLAlchemy(app)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/about')
# def about():
#     return render_template('about.html')

# @app.route('/post')
# def post():
#     return render_template('post.html')

# @app.route('/contact')
# def contact():
#     return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)