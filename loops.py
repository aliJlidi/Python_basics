#exmple of loops 

def main():
    x =0 
    #define a while loop 
    while(x<5):
        print(x)
        x+=1

    #define a for loop 
    for x in range(5,10):
        print(x)

    #use a for loop over a collection 
    days=["Mon", "Tue", "Thu", "Fri", "Sat", "Sun"]
    for i,d in enumerate(days):
         print(i,d)
    
    # use the continue and the break statements
    for x in range(5,10):
        #if(x==7):break
        if(x%2 == 0): continue
        print(x)
if(__name__ == "__main__"):
    main()