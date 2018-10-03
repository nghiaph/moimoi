from application.mongodb.mongo_connect import mongo

"""
    Grouping devices which is assigned to user(s), included:
    - Lab name.
    - Number of devices.
    - Device ids.
    - Authorized user.
"""


class Group:
    def __init__(self, group_name):
        # For admin (privilege = 1)
        temp_group = mongo.db.group.find_one({'group_name': group_name})
        self.group_name = temp_group['group_name']
        self.list_username = temp_group['list_username']
        self.list_devic_ip = temp_group['list_device_ip']
        self.date = temp_group['date']
        self.last = temp_group['last']
