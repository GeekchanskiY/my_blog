from flask import Blueprint, render_template, request
import random


blog_bp = Blueprint('blog', __name__, template_folder='templates/blog', url_prefix='/blog')


@blog_bp.before_request
def add_request_id():
    request.request_id = random.randint(1000, 9999)
    # save to database

@blog_bp.route("/post/<post_id>", methods=['GET'])
def blog_post(post_id):
    print("User name from cookie:", request.cookies.get('user_name'))

    return render_template('blog/post.html', post_id=post_id, username=request.request_user)


@blog_bp.route("/add_post", methods=['GET', 'POST'])
def add_post():
    print("Request ID:", request.request_id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        return render_template('blog/post.html', post_id=title)

    return render_template('blog/add_post.html', username=request.request_user)
