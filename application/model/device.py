from application.mongodb.mongo_connect import mongo
"""
    Type of stored device:
        0: cisco_ios
        1: 
        2: cisco_xr
        3: cisco_asa
"""

class Device:
    def __init__(self, ip):
        temp_device = mongo.db.device.find_one({'ip': ip})
        self.ip = temp_device['ip']
        self.hostname = temp_device['hostname']
        self.username = temp_device['username']
        self.password = temp_device['password']
        self.device_type = temp_device['device_type']