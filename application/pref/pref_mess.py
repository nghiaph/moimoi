"""
    Storing preference messages

"""

# On Login session
UM_LOGIN_ERR = "Username or Password is invalid!!"
UM_LOGIN_SUCC = "Login successful!! "

# On Registration session
UM_REG_ERR = "Registration error: Username is not available!!"
UM_REG_SUCC = "Registered!!"

# On Remove user session
UM_RM_USER_NOT_AUTHORIZED = "You are not authorized to remove user"
UM_RM_USER_ERR = "The username is not valid!!"
UM_RM_USER_SUCC = "The user has been removed from database"

# On Device manager session
DM_IS_SSH = '_ssh'
DM_IS_TELNET = '_telnet'
DM_SSH_NOR_TELNET = 'The device is not configured to allow ssh nor telnet connection'
DM_UNREACHABLE = 'The device is unreachable!!'
DM_REACHABLE = 'Connection to the device is available'
DM_IS_NOT_AVAILABLE = 'The device is not available'
DM_RM_SUCC = 'The device has been removed!!'

