from system.core.model import Model
from flask import Flask, flash, session
import re

# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[a-zA-Z]*$')
                        #is there upper case, number, at least 8 charater
PW_REGEX = re.compile(r'^(?=.*?[A-Z])(?=.*?\d)[A-Za-z\d]{8,}$')
NOSPACE_REGEX = re.compile(r'^[a-zA-Z0-9]*$')

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

    def get_user_email(self, email):
        # pass data to the query like so
        print "I reached get_user_email model"
        data = { 'email': email}
        query = "SELECT * FROM users WHERE email = :email"
        return self.db.query_db(query, data)


        # # pass data to the query like so
        # query = "SELECT * FROM courses WHERE id = :course_id"
        # data = { 'course_id': course_id}
        # return self.db.query_db(query, data)