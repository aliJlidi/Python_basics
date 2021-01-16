#working wiht os.path module
import os
from os import path
import datetime
from datetime import date, time, timedelta
import time 

def main():
    #print the name of the os
    print(os.name)
#check for item exist
    print("Item exists: " + str(path.exists("textfile.txt")))

#work with file paths
    print("Item path: " + str(path.realpath("textfile.txt")))
    print("Item path and name: " + str(path.split(path.realpath("textfile.txt"))))

#get the modification time 
    t =time.ctime(path.getmtime("textfile.txt"))
    print(t)
    print(datetime.datetime.fromtimestamp(path.getmtime("textfile.txt")))

if (__name__ == "__main__"):
    main()