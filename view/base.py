from flask import Blueprint, render_template, request
from controller.base import BaseController

controller = BaseController()
base_bp = Blueprint('base', __name__)


@base_bp.route("/", methods=['GET'])
def index():
    data = controller.index()
    
    return render_template('blog/index.html', post_ids=data, username=request.request_user)


