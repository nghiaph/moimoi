from flask import render_template, request, flash
#from flask_login import login_required, current_user
from application import app
from application.user_management.user_management import AccountMgmt


@app.route('/')
@app.route('/login')
@app.route('/index')
def index():
    return render_template('login.html')


@app.route('/home', methods=["POST"])
#@login_required
def user_authen():
    username = request.form['username']
    password = request.form['password']
#    current_user = User(username)
    user = AccountMgmt()
    if user.authen(username, password) is True:
        return render_template('home.html', username=username)
    else:
        flash(user.authen(username, password))
        return render_template('login.html')


@app.route('/home#add_user', methods=["POST"])
def add_user():
    username = request.form['adduser_username']
    password = request.form['adduser_password']
    confirm_password = request.form['adduser_confirm_password']
    privilege = request.form['adduser_privilege']
    add = AccountMgmt()
    if password == confirm_password:
        add.guest_reg(username, password, privilege)
    return username + password + privilege


@app.route('/home#remove_user', methods=["POST"])
def rm_user():
    username = request.form['rmuser_username']
    rm = AccountMgmt()
    return rm.remove_user(username)


@app.route('/home#add_device', methods=["POST"])
def add_device():
    pass


@app.route('/home#rm_device', methods=["POST"])
def rm_device():
    pass

