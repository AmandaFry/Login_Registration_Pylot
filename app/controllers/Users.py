from system.core.controller import *
from flask import Flask, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NOSPACE_REGEX = re.compile(r'^[a-zA-Z0-9]*$')

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        # Note that we have to load the model before using it in the methods below
        self.load_model('Loginreg')

    # method to display registration page
    def index(self):
        return self.load_view('index.html')

    def process(self):
        session['email'] = request.form['email']
        session['password'] = request.form['passw']

        #check to see if both field has at least two entry
        if len(session['email'])<2 or len(session['password'])<2:
            flash("email or password was too short")
            return redirect('/')
        #check to see if email has an email format
        elif not EMAIL_REGEX.match(session['email']):
            flash("Please enter a valid email format")
            return redirect('/')
        # check to see if any of the entry is only spaces
        elif not NOSPACE_REGEX.match(session['password']):
            flash("Email or password did not match")
            return redirect('/')
        else:
            users = self.models['Loginreg'].get_user_email(session['email'])
            print users
            return self.load_view('success.html', users=users)

    # def success(self):
    #     # return self.load_view('success.html', email=session['email'], passw=session['password'])
    #     return self.load_view('success.html')

    def logout(self):
        session.clear()
        return redirect('/')

    # def create(self):
    #     #register a new user - gather data posted to our create method and format it to pass it to the model
    #     user_info = {
    #         'f_name':request.form['f_name'],
    #         'l_name':request.form['l_name'],
    #         'email':request.form['email'],
    #         'passw':request.form['passw'],
    #         'conf_passw':request.form['conf_passw'],
    #     }
    #     # call create_user method from model and write some logic based on the returned value
    #     # notice how we passed the user_info to our model method
    #     create_status = self.models['User'].create_user(user_info)

    #     create_status = self.models['User'].create_user(user_info)
    #     if create_status['status'] == True:
    #         # the user should have been created in the model
    #         # we can set the newly-created users id and name to session
    #         session['id'] = create_status['user']['id'] 
    #         # session['name'] = create_status['user']['name']
    #         # we can redirect to the users profile page here
    #         return redirect('/users')
    #     else:
    #         # set flashed error messages here from the error messages we returned from the Model
    #         for message in create_status['errors']:
    #             flash(message, 'regis_errors')
    #         # redirect to the method that renders the form
    #         return redirect('/users/new')

