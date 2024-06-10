from flask import Flask, render_template, request, redirect, url_for
import markdown
import os

app = Flask(__name__)
blog_posts = {}

@app.route('/')
def index():
    return render_template('index.html', posts=blog_posts)

@app.route('/new_post', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        blog_posts[title] = content
        return redirect(url_for('index'))
    return render_template('new_post.html')

@app.route('/edit_post/<title>', methods=['GET', 'POST'])
def edit_post(title):
    if request.method == 'POST':
        content = request.form['content']
        blog_posts[title] = content
        return redirect(url_for('index'))
    return render_template('edit_post.html', title=title, content=blog_posts[title])

@app.route('/delete_post/<title>', methods=['POST'])
def delete_post(title):
    del blog_posts[title]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
