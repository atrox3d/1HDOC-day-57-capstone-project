from flask import Flask, render_template
import util.network, util.api as api

app = Flask(__name__)


@app.route('/')
def home():
    posts = api.get_posts()
    return render_template("index.html", posts=posts)


if __name__ == "__main__":
    app.run(debug=True, host=util.network.get_ipaddress())
