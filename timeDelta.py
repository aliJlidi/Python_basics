#working with dates 
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

#construct a basic timedelta and print

print(timedelta(days=365, hours=5, minutes=1))

#Today date
now = datetime.now()
print("Today is "+ str(now))

#print todays date one year from now
print("One year from now : ", str(now+timedelta(days=365)))

#create a timedelta that use more than argument
print("In tow days and three weeks, it will be "+
         str(now+timedelta(days=2, weeks=3)))
# create a timecelta a week ago
t= datetime.now()- timedelta(weeks=1)
s= t.strftime("%A %B %d, %Y") 
print("One week ago it was : " + s)
#How many days until april fool's day
today = date.today() # get today date
aprilFoolDay = date(today.year, 4, 1) # get april fool day
      #use date comparison to see if April Fool's has already gone
      #if it has, use the replace() function to get the date of the next year
if aprilFoolDay< today: # comparing if april fool day is passed
    print("April Fool's day already went by %d days ago " %((today-aprilFoolDay).days))
    aprilFoolDay = aprilFoolDay.replace(year= today.year+1)

# calculate the amount of time until April Fool's day
timeToAprilFoolDay = aprilFoolDay - today
print("It's just ", timeToAprilFoolDay,"days until April fool's days")
def main():
   print("this is main function")
   


if(__name__=="__main__"):
    main()