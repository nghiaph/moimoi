from application.mongodb.mongo_connect import mongo
"""
    User level privileged:
        - 0: Developer
        - 1: Mighty Admin
        - 2: Admin
        - 3: Cisco user
        - 4: Guest user
"""

class User:
    def __init__(self, username):
        temp_user = mongo.db.user.find_one({'username': username})
        self.username = temp_user['username']
        self.password = temp_user['password']
        self.privilege = temp_user['privilege']
        self.group_id = temp_user['group_id']
