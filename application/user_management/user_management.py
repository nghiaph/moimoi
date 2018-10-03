from application.mongodb.mongo_connect import mongo
from application.pref.pref_mess import UM_LOGIN_ERR, UM_REG_SUCC, UM_REG_ERR, \
    UM_RM_USER_ERR, UM_RM_USER_SUCC

"""
    User level privileged:
        - 0: Developer
        - 1: Admin
        - 2: Cisco user
        - 3: Guest user
"""


class AccountMgmt:
    # Authentication part
    def authen(self, username, password):
        if mongo.db.user.find_one({"username": username}) is not None \
        and mongo.db.user.find_one({"password": password}) is not None:
            return True
        else:
            return UM_LOGIN_ERR

    # Registration part
    def guest_reg(self, username, password, privilege):
        if self.check_valid(username) is True:
            coll_user = {
                "username": username,
                "password": password,
                "privilege": privilege,
            }
            mongo.db.user.insert_one(coll_user)
            print(UM_REG_SUCC)
            return UM_REG_SUCC
        else:
            print(UM_REG_ERR)
            #        mongo.db.user.update({"username": username}, {"$set": {"privilege": privilege}})
            return UM_REG_ERR

    def check_valid(self, username):
        count = 0
        for user in mongo.db.user.find({'username': username}):
            count = count + 1
        if count == 0:
            return True
        return False

    # Remove user
    def remove_user(self, username):
        if self.check_valid(username) is True:
            mongo.db.user.delete_one({'username': username})
            return UM_RM_USER_SUCC
        else:
            return UM_RM_USER_ERR

    def get_privilege(self, username):
        for user in mongo.db.user.find({'username': username}):
            return user['privilege']
