from flask import Flask, render_template

import data

app = Flask(__name__)

@app.route('/')
def index():
    posts = data.lire_posts()
    return render_template('index.html', posts = posts)

@app.route('/<int:post_id>')
def post(posit_id):
    posts = data.get_posts(post_id)
    return render_template('post.html', post = post)


if __name__ == "__main":
    app.run(dabug=True)
