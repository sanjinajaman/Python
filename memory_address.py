a=2
print("memory address",id(2))
print("memory address",id(a))
a=2
print("memory address a=",id(a))
a=a+1
print("memory address a=",id(a))
b=4
print("memory address b=",id(b))
print("memory address ",id(4))

a="hello"
print(id(a))