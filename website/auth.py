from flask import Blueprint, render_template, request, flash, redirect, url_for, send_from_directory, abort
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
#NOTE FOR current_user - uses UserMixin library to access information about current user
from flask_login import login_user, login_required ,logout_user, current_user

import os
import shutil

import uuid as uuid

from .models import User
from . import db

auth = Blueprint('auth', __name__)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.signin'))

@auth.route('/sign-in',methods=['GET','POST'])
def signin():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                #Remembers that user is logged in - until cache is deleted
                login_user(user, remember=True)

                return redirect(url_for('views.home'))
            else:
                flash('Username or password is not valid',category="error")
        else:
            flash('Username or password is not valid',category="error")


    return render_template("signin.html")

@auth.route('/create-account',methods=['GET','POST'])
def Register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        passwordcnfrm = request.form.get('passwordcnfrm')
        checkthisout = request.form.get('checkthisout')

        user = User.query.filter_by(username=username).first()
        if user:
            flash("This username is taken",category="error")
        else:
            user = User.query.filter_by(email=email).first()
            if user:
                flash("This email is taken",category="error")
            else:
                if password != passwordcnfrm:
                    flash("Passwords don't match, please try again.", category='error')
                else:
                    new_user = User(email=email,username=username, password=generate_password_hash(password, method="sha256") )
                    db.session.add(new_user)
                    db.session.commit()
                    flash('Account created!', category='success')
                    #Find the user


    return render_template("register.html",methods=['GET','POST'])

@auth.route('/profile',methods=['GET','POST'])
@login_required
def Profile():
    user = current_user
    allowed_extensions = ['jpg','png']
    edit = "0"
    if request.method == "POST":
        edit = request.form.get('edit')
        if edit == "0":
            name = request.form.get('name')
            surname = request.form.get('surname')
            photo = request.files['photo']
            get_file_value = request.form.get('change_photo')
            print(f'\n\n\n{get_file_value}\n{photo}\n\n\n')

            if photo:
                if photo.filename.split('.')[1] in allowed_extensions:
                    if str(user.photoname) != 'None':
                        os.remove(os.path.join('website\\static\\data',str(user.photoname)))

                    filename = secure_filename(photo.filename)
                    uuid_string = str(uuid.uuid1()) + f'_{filename}'
                    photo.save(os.path.join('website\\static\\data',uuid_string))
                    user.photoname = uuid_string
                else:
                    #TODO flash error
                    print('Extension not allowed')


            user.name = name
            user.surname = surname
            db.session.commit()

    return render_template("profile.html",user=current_user, edit=edit, methods=['GET','POST'])
