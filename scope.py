#scope
x=4

def func():
    global x
    x=2 #local variable
    print(x)
    return x

print(x)
print(func())
#def func2():
   #print(x)
print(x)


