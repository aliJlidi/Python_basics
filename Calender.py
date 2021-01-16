#Working wiht calendar 
import calendar 

#create a plain text calendar
c= calendar.TextCalendar(calendar.MONDAY)
st= c.formatmonth(2021,1,0,0)
print(st)

#create an HTML formatted calendar
hc = calendar.HTMLCalendar(calendar.SUNDAY)
st2= hc.formatmonth(2021,1)
#create an empty file called index
Html_file= open("index","w")
#add sting inside it
Html_file.write(st2)
#save and close it 
Html_file.close()
#print(st2)

#loops over the days of the month
for i in c.itermonthdays(2021, 8):
    print(i)

#The names of days and months in full and abbreviated forms
for name in calendar.month_name:
    print(name)

for day in calendar.day_name:
    print(day)

#Calculate days based a rule:
#meet each friday of the next year month
print("Team meeting will be on : ")
for m in range(1,13):
    cal=calendar.monthcalendar(2022,m)
    weekone = cal[0]
    weektwo = cal[1]

    if(weekone[calendar.FRIDAY] !=0):
        meetDay = weekone[calendar.FRIDAY]
    else:
        meetDay = weektwo[calendar.FRIDAY]

    print("%10s %2d "%(calendar.month_name[m], meetDay))
