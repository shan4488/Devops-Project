""" All the database operations will be carried in this file """
from uuid import uuid4
import pymongo
from flask import request



client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
userdb = client['devops']
users = userdb.user


def insert_data():
    """ Insert the registered user data to the database """
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['pass']
        
        reg_user = {}
        reg_user['name'] = name
        reg_user['email'] = email
        reg_user['password'] = password
        reg_user['token'] = str(uuid4())
        reg_user['devices'] = {}
        
        if users.find_one({"email":email}) is None:
            users.insert_one(reg_user)
            return True
        else:
            return False


def check_user():
	""" Check whether the user is registered """
	if request.method == 'POST':
		email = request.form['email']
		password = request.form['pass']

		user = {
			"email": email,
			"password": password
		}

		user_data = users.find_one(user)
		if user_data is None:
			return False, ""
		else:
			return True, user_data["name"], user_data["token"]
		