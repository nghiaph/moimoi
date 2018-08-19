# Package for managing devices
from netmiko import ConnectHandler
import pexpect

# Preference variables, messages, commands,...
from application.model.device import Device
from application.mongodb.mongo_connect import mongo
from application.pref.pref_cmd import CMD_PING, CMD_SSH, CMD_TELNET
from application.pref.pref_mess import DM_IS_SSH, DM_IS_TELNET, DM_UNREACHABLE, DM_SSH_NOR_TELNET, DM_REACHABLE, \
    DM_IS_NOT_AVAILABLE, DM_RM_SUCC


class DeviceMgmt:
    def __init__(self, ip):
        self.current_device = Device(ip)
        if self.is_ssh_or_telnet() == DM_IS_SSH:
            self.device = {
                'device_type': self.current_device.device_type,
                'ip': self.current_device.ip,
                'hostname': self.current_device.hostname,
                'username': self.current_device.username,
                'password': self.current_device.password,
            }
        elif self.is_ssh_or_telnet() == DM_IS_TELNET:
            self.current_device.device_type = self.current_device.device_type + self.is_ssh_or_telnet()
            self.device = {
                'device_type': self.current_device.device_type,
                'ip': self.current_device.ip,
                'hostname': self.current_device.hostname,
                'username': self.current_device.username,
                'password': self.current_device.password,
            }
        elif self.is_reachable() == DM_REACHABLE and self.is_ssh_or_telnet() == DM_SSH_NOR_TELNET:
            self.is_ssh_or_telnet()
        else:
            self.is_reachable()
        self.net_connect = ConnectHandler(**self.device)

    # Checking connection to the device
    def is_reachable(self):
        ping = pexpect.spawn(CMD_PING + self.current_device.ip)
        result = ping.expect(['64 bytes', pexpect.EOF, pexpect.TIMEOUT])
        if result == 2:
            return DM_UNREACHABLE
        return DM_REACHABLE

    # Checking is ssh or telnet available on device
    def is_ssh_or_telnet(self):
        ssh = pexpect.spawn(CMD_SSH + self.current_device.username + '@' + self.current_device.ip)
        result = ssh.expect(['username: ', pexpect.TIMEOUT])
        if result == 1:
            return DM_IS_SSH
        else:
            telnet = pexpect.spawn(CMD_TELNET + self.current_device.ip)
            result = telnet.expect(['username: ', pexpect.TIMEOUT])
            if result == 1:
                return DM_IS_TELNET
            else:
                return DM_SSH_NOR_TELNET

    def is_available(self, ip):
        count = 0
        for device in mongo.db.device.find({'ip': ip}):
            count += 1
        if count == 0:
            return True
        return False

    def add_device(self, ip, username, password, device_type, serial, rack_mount):
        pass

    def remove_device(self, ip):
        if self.is_available(ip) is False:
            return DM_IS_NOT_AVAILABLE
        else:
            mongo.db.device.delete_one({'ip': ip})
        return DM_RM_SUCC
