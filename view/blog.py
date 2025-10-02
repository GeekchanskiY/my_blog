from flask import Blueprint, render_template, request, redirect, url_for
from model.models import BlogItem
from db import Session
import random


blog_bp = Blueprint('blog', __name__, template_folder='templates/blog', url_prefix='/blog')


@blog_bp.before_request
def add_request_id():
    request.request_id = random.randint(1000, 9999)


@blog_bp.route("/post/<post_id>", methods=['GET'])
def blog_post(post_id):
    return render_template('blog/post.html', post_id=post_id, username=request.request_user)


@blog_bp.route("/add_post", methods=['GET', 'POST'])
def add_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title or not content:
            return "Title and content cannot be empty", 400
        
        with Session as session:
            new_post = BlogItem(title=title, content=content)

            session.add(new_post)

            session.commit()

            session.refresh(new_post)

        return redirect(url_for('blog.blog_post', post_id=new_post.id))

    return render_template('blog/add_post.html', username=request.request_user)
