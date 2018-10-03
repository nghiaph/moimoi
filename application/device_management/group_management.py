from application.mongodb.mongo_connect import mongo
from application.model.user import User
from application.model.device import Device
from application.model.group import Group

"""
    Managing group of devices that assigned to user(s)
"""

class GroupMgmt:
    def create_group(self, user:User, device:Device):
       pass
