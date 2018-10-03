# Importing Flask package
from flask import render_template, request, flash

# Import preference variables
from application import app
from application.pref import pref_static_vars, pref_objects

# Importing models
from application.model.user import User

# Importing management functions
from application.user_management.user_management import AccountMgmt


@app.route('/')
@app.route('/login')
@app.route('/index')
def index():
    return render_template('login.html')


@app.route('/home', methods=["POST"])
def user_authen():
    username = request.form['username']
    password = request.form['password']
    pref_objects.current_user = User(username)
    mgmt = AccountMgmt()
    if mgmt.authen(username, password) is True:
        if 0 < pref_objects.current_user.privilege <= 2:
            return render_template('home_admin.html', username=username)
        elif pref_objects.current_user.privilege > 2:
            return render_template('home_user.html', username=username)
        else:
            return render_template('home_dev.html', username=username)
    else:
        flash(mgmt.authen(username, password))
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


@app.route('/show_list_user', methods=["POST"])
def show_list_user():
    pass