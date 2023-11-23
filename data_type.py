a=5
b=7.8
c=5+5j

print(type(a),isinstance(a,complex)) #instance function check this data type is true or false
print(type(a),isinstance(a,int))


print(type(b),isinstance(b,complex))
print(type(b),isinstance(b,float))

print(type(c) ,isinstance(c,complex))

print("python list")

a=[1,3.4,'sanjina'] #this is a list this list items do not need a same data type
print(a)
print("a[2]=", a[2])

a=[1,5,10,15,20,25,30,40,50,60]

print("a[3:]",a[3:])#this line print of this list starting printing after 3 element
print("a[0:3]",a[0:3])#this line print of this list first 3 element
print("a[4]=",a[4])

print("==MUTABLE==")

x=[1,5,10,20]
print(x)
x[3]=15
print(x)

print("==TUPLE==")


a=(1,3.4,'sanjina')
print(a)
print("a[2:0]",a[2:0]) #empty

print("a[2:1]",a[2:1])#empty
print("a[2:0]",a[2:])#this line print the list after 2 element
print("a[0:1]",a[0:1])# this line print first element
#a[0]=10 tuple object does not support item assignment
print(a)

print("==String==")
s="my name is sanjina"
print(s)

print("==set==")
a={1,3,4,5,6}
b=[1,4,3,5,6]
c=(1,4,3,5,6)
print(b)
print(a)
print(c)
print(type(a))
print(type(b))
print(type(c))




