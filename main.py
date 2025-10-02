from flask import Flask, request, jsonify, render_template
from view.base import base_bp
from view.blog import blog_bp
from view.user import user_bp
import werkzeug.exceptions as exceptions


app = Flask(__name__)

@app.errorhandler(exceptions.HTTPException)
def handle_bad_request(e):
    return render_template('400.html', error=e), 400

@app.before_request
def add_request_id():
    username = request.cookies.get('user_name', None)

    request.request_user = username

app.register_blueprint(base_bp)
app.register_blueprint(blog_bp)
app.register_blueprint(user_bp)

@app.route("/health", methods=['GET'])
def health_check():
    return jsonify(
        {"status": "OK",}
    ), 200
