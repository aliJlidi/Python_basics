# working with files

def main():
    # open a file
    #f = open("textfile.txt","w+")
    # open a file to append text to the end
    f = open("textfile.txt","r")
    #writing some lines of data
    """
    for i in range(10):
        f.write("This is line "+ str(i)+ "\r\n")
"""
    #close the file when done
    #f.close()
    #open the file back up and read the contents
    if (f.mode == "r"):
        #contents = f.read()
        fl= f.readlines()
        for x in fl:
              print(x)





if(__name__ == "__main__"):
    main()