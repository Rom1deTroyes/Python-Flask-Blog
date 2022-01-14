from flask import Flask, render_template

import data

app = Flask(__name__)

@app.route('/')
def index():
    posts = data.lire_posts()
    return render_template('index.html', posts = posts)

if __name__ == "__main":
    app.run(dabug=True)
