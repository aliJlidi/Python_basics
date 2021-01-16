#working with dates 
from datetime import datetime 


def main():
    now =datetime.now()
    print(now.strftime("The current year is: %Y"))
    #%Y year , %A weekday, %B month, %D day of month
    print(now.strftime("%a, %d %B, %y"))
    #local date and time
    print(now.strftime("Local date and time: %c"))
    print(now.strftime("Local time is: %X"))
    ## TIme FOrmating##
    print(now.strftime("The current Time is: %I:%M:%S %p"))


if(__name__=="__main__"):
    main()