from flask import Flask, render_template, url_for
import util.network, util.api as api
import json

app = Flask(__name__)


@app.route('/')
def home():
    posts = api.get_posts()
    return render_template("index.html", posts=posts)


@app.route('/post/<post_id>')
def read_post(post_id):
    post = [post for post in api.get_posts() if post.id == int(post_id)][0]
    return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(debug=True, host=util.network.get_ipaddress())
