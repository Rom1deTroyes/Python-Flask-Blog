from flask import Flask, render_template, request

import data

app = Flask(__name__)

@app.route('/')
def index():
    posts = data.lire_posts()
    return render_template('index.html', posts = posts)

@app.route('/<int:post_id>')
def post(post_id):
    post = data.get_post(post_id)
    return render_template('post.html', post = post)

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/add', methods=['GET'])
def add():
    title = request.values.get('title')
    content = request.values.get('content')
    data.set_post(title, content)
    return render_template('add.html')

if __name__ == "__main":
    app.run(dabug=True)
