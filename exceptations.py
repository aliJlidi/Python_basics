from cgitb import reset


import sys

try:

    x = int(input("x: "))
    y= int(input("y: "))

except ValueError:
    print('invalid input')
    sys.exit(1)


try:
    result = x/y 

except ZeroDivisionError:
    print('error : can not devide by zero')
    sys.exit(1)


print(f"{x} / {y} = {result}")