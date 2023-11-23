x = 5  #here x is integer type data storing
y ='sanjina' #here y is string type data storing
z ="sanjina" #here z is string type data storing
print(x)
print(y)
print(z)


print("2nd part ")
x=5  #x is strore integer type data
x="sanjina" #now x is store string type data

print(x) #here this line print sanjina

print ("type casting")
x=str(3) #here x is '3'
y=int(3) #here y is 3
z=float(3.0)  #here z is 3.0

print(x)
print(y)
print(z)

print("type () function")
x=5
y="sanjina"
z=3.50
print(type(x))
print(type(y))
print(type(z))

print("Single Quotes & double Quotes work as same")
x='sanjina'
y="sanjina"
# here x & y is same as
print(x)
print(y)

print("case sensitive")

a=5
A=6
#here A not overwrite a they are individual
print(a)
print(A)

name,age="sanjina",'20'
print("Hi "+name+" Your age is "+age)
print(age)
print(name)
x=y=z=2
print(x+y+z)

name,age=input("enter your name and age:").split(",") #take input like sanjina , 20
print(name)
print(age)
print(name,age)





