from app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 


class User:
    db_name = 'week8'
    def __init__(self, data):
        self.id = data['id']
        self.firstName = data['firstName']
        self.lastName = data['lastName']
        self.email = data['email']
        self.password = data['password']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']

    @staticmethod
    def validate(user):
        isValid = True
        query = "SELECT * FROM user WHERE email = %(email)s;"
        results = connectToMySQL(User.db_name).query_db(query,user)
        if len(results) > 1:
            isValid = False
            flash("That email is already in the system!")
        if len(user['password']) < 6:
            isValid = False
            flash("Password must be at least 6 characters long")
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid Email!!!")
            isValid=False
        if len(user['firstName']) < 2:
            isValid = False 
            flash("First name must be at least 2 characters long")
        if len(user['lastName']) < 2:
            isValid = False 
            flash("Last name must be at least 2 characters long")
        if user['password'] != user['confirm']:
            isValid = False
            flash("Your Passwords don't match")

        return isValid

    @classmethod
    def save(cls, data):
        query = "INSERT INTO user (firstName, lastName, email, password) VALUES (%(firstName)s, %(lastName)s, %(email)s, %(password)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)


    @classmethod
    def getAll(cls):
        query = "SELECT * FROM user;"
        results = connectToMySQL(cls.db_name).query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def getOne(cls, data):
        query = "SELECT * FROM user WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def getEmail(cls, data):
        query = "SELECT * FROM user WHERE email = %(email)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def update(cls, data):
        q = "UPDATE user SET firstName=%(firstName)s, lastName=%(lastName)s, WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(q, data)
    
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM user WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

# instance method
    def fullName(self):
        return f"{self.firstName} {self.lastName}"

    
    