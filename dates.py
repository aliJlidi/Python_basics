#working with dates 
from datetime import date
from datetime import time
from datetime import datetime

def main():
    td = date.today()
    print("Today is : ", td)

#print date compentes
    print("Date components : ",td.day, td.month, td.year)

#recieve weekday 
    print("Today weekday is ", td.weekday())
    days=["mon", "tue","wed","thu","fri","sat","sun"]
    print("Which is a : ", days[td.weekday()])

# get todya date from datetime class
    print("the current time is : ", datetime.time(datetime.now()))


if(__name__=="__main__"):
    main()    