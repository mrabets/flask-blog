from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


if app.config["ENV"] == "production":
    app.config.from_object("config.ProductionConfig")
else:
    app.config.from_object("config.DevelopmentConfig")

db = SQLAlchemy(app)

from simple_page.blueprint import simple_page
from blog_post.blueprint import blog_post

app.register_blueprint(simple_page)
app.register_blueprint(blog_post)

if __name__ == '__main__':
    app.run(debug=True)