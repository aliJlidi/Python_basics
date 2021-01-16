
f=0
print(f)
k ="abc"
print(k)
print("this is a string" + str(123))

def someFunc():
    global f
    f="def"
    print(f)

someFunc()
print(f)