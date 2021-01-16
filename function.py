#basic function
def func1():
    print("I'm a function")
#function that takes arguments
def func2(arg1, arg2):
    print(arg1, " ",arg2)

#function that returns a value
def cube(x):
    return print(pow(x,3))
#function with default argument
def power(num,p=1):  
    result = 1 
    for i in range(p):
        result = result * num 
        i/=1
    return result
#function with variable number of arguments
def multi_add(*args):
    result = 0 
    for x in args:
        result = result + x
    return result

cube(3)
#func1()
#print(func1())
#print(func1)
#func2(10,20)
#print(func2(20,30))
print(power(2))
print(power(2,3))
print(multi_add(10,5,78,10,25))