from application.mongodb.mongo_connect import mongo
"""
    User level privileged:
        - 0: Developer
        - 1: Admin
        - 2: Cisco user
        - 3: Guest user
"""

class User:
    def __init__(self, username):
        temp_user = mongo.db.user.find_one({'username': username})
        self.username = temp_user['username']
        self.password = temp_user['password']
        self.privilege = temp_user['privilege']
