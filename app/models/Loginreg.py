from system.core.model import Model
from flask import Flask, flash, session
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NOSPACE_REGEX = re.compile(r'^[a-zA-Z0-9]*$')


# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
# NAME_REGEX = re.compile(r'^[a-zA-Z]*$')
                        #is there upper case, number, at least 8 charater
PW_REGEX = re.compile(r'^(?=.*?[A-Z])(?=.*?\d)[A-Za-z\d]{8,}$')
# NOSPACE_REGEX = re.compile(r'^[a-zA-Z0-9]*$')

class Loginreg(Model):
    def __init__(self):
        super(Loginreg, self).__init__()
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
    def get_all_users(self):
        print "I reached get_all_users model"
        query = "SELECT * from users"

        return self.db.query_db(query)

    def get_user_email(self, user_info):
        # pass data to the query like so
        print "I reached get_user_email model"
        errors=[]
        #check to see if both field has at least two entry
        if len(user_info['email'])<2 or len(user_info['password'])<2:
            errors.append("email or password was too short")
            # return redirect('/')
        #check to see if email has an email format
        elif not EMAIL_REGEX.match(user_info['email']):
            errors.append("Please enter a valid email format")
            # return redirect('/')
        # check to see if any of the entry is only spaces
        elif not NOSPACE_REGEX.match(user_info['password']):
            errors.append("Email or password did not match")
            # return redirect('/')
        if errors:
            print errors
            return {"status": False, "errors": errors}
        else:
            data = { 'email': user_info['email']}
            query = "SELECT * FROM users WHERE email = :email"
            users = self.db.query_db(query, data)
            # return { "status": True, "users": users[0] }
            if len(users) == 0:
                errors.append("User was not found please register")
            else:
                return { "status": True, "users": users[0] }
                # return (users[0])
            return (users)


        # # pass data to the query like so
        # query = "SELECT * FROM courses WHERE id = :course_id"
        # data = { 'course_id': course_id}
        # return self.db.query_db(query, data)