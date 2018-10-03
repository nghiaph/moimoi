from application.mongodb.mongo_connect import mongo
"""
    Type of stored device:
        0: cisco_ios
        1: cisco_xr (xe)
        2: cisco_asa
        3: 
"""


class Device:
    def __init__(self, ip):
        temp_device = mongo.db.device.find_one({'ip': ip})
        self.ip = temp_device['ip']
        self.hostname = temp_device['hostname']
        self.username = temp_device['username']
        self.password = temp_device['password']
        self.device_type = temp_device['device_type']
        self.serial = temp_device['serial']
        self.os_version = temp_device['os_version']
        self.group_id = temp_device['group_id']

