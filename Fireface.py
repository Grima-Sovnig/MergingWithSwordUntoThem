import os
import platform

def fireFoxWalk():
    # Sets the current user, and OS type
    currentUser =  os.getlogin()
    osType = platform.system()
    # Initializes the key and login files, also declares the starting path to look for those files.
    keyFile, loginFile = "/", "/"
    windowsWalk = "C:\\Users\\" + currentUser + "\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\"
    linuxWalk = '/home/' + currentUser + ''
    macWalk = '/Users/' + currentUser + '/Library/Application Support/Firefox/Profiles/'
    
    
    if osType == "Linux":
        for root, dirs, files in os.walk(linuxWalk):
            for name in files:
                if name =='key4.db':
                    keyFile = os.path.abspath(os.path.join(root, name))
                if name =='logins.json':
                    loginFile = os.path.abspath(os.path.join(root, name))
    if osType == "Windows":
        for root, dirs, files in os.walk(windowsWalk):
            for name in files:
                if name =='key4.db':
                    keyFile = os.path.abspath(os.path.join(root, name))
                if name =='logins.json':
                    loginFile = os.path.abspath(os.path.join(root, name))
    if osType == "Darwin":
        for root, dirs, files in os.walk(windowsWalk):
            for name in files:
                if name =='key4.db':
                    keyFile = os.path.abspath(os.path.join(root, name))
                if name =='logins.json':
                    loginFile = os.path.abspath(os.path.join(root, name))
    # Returns the file path of the key and logins files.
    return keyFile, loginFile