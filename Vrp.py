import random
#input the number of cities 
#cities = int(input('Number of cities : '))
cities = 10
#couriers = input ('Number of couriers : ')
couriers = 4


while True:
   xpoints =[0]
   ypoints =[0]
   points = [[0,0]]
   for i in range(0,cities):
       x = random.randint(1,cities)
       y = random.randint(1, cities)
       xpoints.append(x)
       ypoints.append(y)
       points.append([xpoints[i+1],ypoints[i+1]])
   
   xset = set(xpoints)
   yset = set(ypoints)
   if((len(xset)==len(xpoints)) or (len(yset)==len(ypoints))):
    break

print(points)
print(points[2])


#1 we randomize a list of the cities index+1
ranList = random.sample(range(cities), cities)
#2 devide the list by the number of couriers 
#3 assign the points to the couriers 
#4 list len(number of couriers) inside it lists of points 