import random
#input the number of cities 
#cities = int(input('Number of cities : '))
cities = 10
#couriers = input ('Number of couriers : ')
numberOfCouriers = 4
couriers = []

while True:
   xpoints =[0]
   ypoints =[0]
   points = [(0,0)]
   for i in range(0,cities):
       x = random.randint(1,cities)
       y = random.randint(1,cities)
       xpoints.append(x)
       ypoints.append(y)
       points.append((xpoints[i+1],ypoints[i+1]))
   
   xset = set(xpoints)
   yset = set(ypoints)
   if((len(xset)==len(xpoints)) or (len(yset)==len(ypoints))):
    break

print("Created points...")
print(points)

#Randomize a list of the cities index (+1 couldn't find a better solution)
ranList = random.sample(range(cities), cities)

#print(ranList)
print("Created ranList...")

# creating the list of couriers
couriers = []
for i in range(0,numberOfCouriers):
    couriers.append([i])

# Setting first location to [0,0]
def appendDepot(numberOfCouriers, couriers, points):
    for i in range(numberOfCouriers):
        couriers[i].append(points[0])

appendDepot(numberOfCouriers, couriers, points)
    

courierIndex = 0


for i in range(cities):
    couriers[courierIndex].append(points[(ranList[i])+1])
    if courierIndex == (numberOfCouriers-1):
       courierIndex = 0
    else:
       courierIndex += 1


# Coming back to depot
appendDepot(numberOfCouriers, couriers, points)

print("Courier 0:")
print(couriers[0])
print(couriers[0][3])
print(couriers[0][3][0])

# Calculating with mannhattan distance
def manhattanDistance(point1, point2):
    distance = 0
    for x1, x2 in zip(point1, point2):
        difference = x2 - x1
        absoluteDifference = abs(difference)
        distance += absoluteDifference

    return distance

print()
print(manhattanDistance((couriers[0][1]),(couriers[0][2])))
print()
print(len(couriers[0]))

distances = []
    
for i in range(numberOfCouriers):
    distances.append(i)
    for j in range(len(couriers[i])-2):
        distances[i]  += manhattanDistance((couriers[i][j+1]),(couriers[i][j+2]))
        

print(distances)
    
    

    


    
#2 devide the list by the number of couriers 
#3 assign the points to the couriers 
#4 list len(number of couriers) inside it lists of points 