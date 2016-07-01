from system.core.model import Model
from flask import Flask, flash, session
import re

# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[a-zA-Z]*$')
                        #is there upper case, number, at least 8 charater
PW_REGEX = re.compile(r'^(?=.*?[A-Z])(?=.*?\d)[A-Za-z\d]{8,}$')

class User(Model):
    def __init__(self):
        super(User, self).__init__()
    """
    Below is an example of a model method that queries the database for all users in a fictitious application
    
    Every model has access to the "self.db.query_db" method which allows you to interact with the database

    def get_users(self):
        query = "SELECT * from users"
        return self.db.query_db(query)

    def get_user(self):
        query = "SELECT * from users where id = :id"
        data = {'id': 1}
        return self.db.get_one(query, data)

    def add_message(self):
        sql = "INSERT into messages (message, created_at, users_id) values(:message, NOW(), :users_id)"
        data = {'message': 'awesome bro', 'users_id': 1}
        self.db.query_db(sql, data)
        return True
    
    def grab_messages(self):
        query = "SELECT * from messages where users_id = :user_id"
        data = {'user_id':1}
        return self.db.query_db(query, data)

    """
    def create_user(self, info):
     # We write our validations in model functions.
    # They will look similar to those we wrote in Flask
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        errors = []
        # Some basic validation
        if not info['f_name']:
            errors.append('First name cannot be blank')
        elif len(info['f_name']) < 2:
            errors.append('First name must be at least 2 characters long')
        if not info['l_name']:
            errors.append('Last name cannot be blank')
        elif len(info['l_name']) < 2:
            errors.append('Last name must be at least 2 characters long')
        if not info['email']:
            errors.append('Email cannot be blank')
        elif not EMAIL_REGEX.match(info['email']):
            errors.append('Email format must be valid!')
        if not info['passw']:
            errors.append('Password cannot be blank')
        elif len(info['passw']) < 8:
            errors.append('Password must be at least 8 characters long')
        elif info['passw'] != info['conf_passw']:
            errors.append('Password and confirmation must match!')
        # If we hit errors, return them, else return True.
        if errors:
            return {"status": False, "errors": errors}
        else:
            # Code to insert user goes here...
            # Then retrieve the last inserted user.
            get_user_query = "SELECT * FROM users ORDER BY id DESC LIMIT 1"
            users = self.db.query_db(get_user_query)
            return { "status": True, "user": users[0] }

    def userLogin(self, user):
        # errors[]
        print "I reached userLogin method"
        query = "SELECT * FROM users WHERE email = '{}' LIMIT 1".format(user['email'])
        userLogin = self.db.query_db(query)
        print userLogin

        # if userLogin == []:
        #     errors.append("User is not valid please resiter")
        # elif len(user_login[0]['username'])<1 or len(user_login[0]['password'])<1:
        #     errors.append('No field can be empty')
        # elif not self.bcrypt.check_password_hash(user_login[0]['password'],user['password']):
        #     errors.append("Invalid password")
        # if errors == []:
        #     session['name'] = user_login[0]['name']
        #     session['username'] = user_login[0]['username']
        #     session['user_id'] = user_login[0]['user_id']
        #     return True
        # else:
        #     for error in errors:
        #         flash(error)
        #     return False;