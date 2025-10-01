from flask import Blueprint, render_template, request, make_response, redirect


user_bp = Blueprint('user', __name__, template_folder='../templates/user', url_prefix='/user')


@user_bp.route("/login", methods=['GET', 'POST'])
def login():
    if request.cookies.get('user_name') is not None:
        return "You are already logged in", 400
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # validate username and password
        # if valid, then set cookie and redirect to home page
        resp = make_response(redirect("/"))
        resp.set_cookie('user_name', username)

        return resp

    return render_template('login.html', username=request.request_user)


@user_bp.route("/logout", methods=['GET'])
def logout():
    resp = make_response(redirect("/"))
    resp.set_cookie('user_name', '', expires=0)

    return resp
