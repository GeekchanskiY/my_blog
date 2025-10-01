from flask import Flask, request, jsonify
from view.base import base_bp
from view.blog import blog_bp
from view.user import user_bp


app = Flask(__name__)

@app.before_request
def add_request_id():
    username = request.cookies.get('user_name', None)
    # request user from database by username
    # if not found, then None

    request.request_user = username

@app.after_request
def add_request_id(resp):
    print("Response Size:", resp.content_length)

    return resp

app.register_blueprint(base_bp)
app.register_blueprint(blog_bp)
app.register_blueprint(user_bp)

@app.route("/health", methods=['GET'])
def health_check():
    return jsonify(
        {"status": "OK",}
    ), 200
