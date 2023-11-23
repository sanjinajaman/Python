first_name='sanjina'
last_name='jaman'

full_name=first_name+last_name
print(full_name)
full_name=first_name+" "+last_name
print(full_name)


first_name='sanjina '
last_name='jaman'
full_name=first_name+last_name
print(full_name)
#print(full_name+3)//type error
print(full_name+"3")
print(full_name+str(3))


first_name='sanjina'
last_name='jaman'
print(full_name*3)
print("===string Formating===")
name,age="sanjina",'20'
print("Hi "+name+" Your age is "+age)
#print("Hi "+name+" Your age is "+age+2) //type error
print("Hi {} Your age is {}".format(name,age))
#print("Hi {} Your age is {}".format(name,age+2)) #type error
print(f"Hi {name} Your age is {age}")
#print(f"Hi {name} Your age is {age+2}") #type error




print("======STRING INDEXING=====")
language ="python"
print(language[0])
print(language[1])
print(language[2])
print(language[3])
print(language[4])
print(language[5])
print("\n\n")

print(language[-6])
print(language[-5])
print(language[-4])
print(language[-3])
print(language[-2])
print(language[-1])


print("=====STRING SLICING=====")
language='python'
print(language[0:4])#syntax----[start argument: stop argument]
print(language[2:4])
print(language[-4:-2])
print(language[2:])
print(language[:3])
#print(language[4:-2])
#print(language[-2:4])


print("====argument=====")
language="python"
print(language[0:5:1])#syntax----[start argument: stop argument:step]

print(language[0:5:2])#syntax----[start argument: stop argument:step]

print(language[0:5:3])#syntax----[start argument: stop argument:step]
print(language[0::2])#syntax----[start argument: stop argument:step]

print(language[0::3])#syntax----[start argument: stop argument:step]
print(language[6::-1])#reverse
print(language[-1::-1])#reverse
print(language[::-1])#reverse


#num=int(1234)
#print(num[0:4:1]) type error



num="1234"
print(num[0:4:1])


print("=====Ex======")
name=input("Enter your name ")
print(f"my name is {name[-1::-1]} ")


name=input("Enter your name ")
print(f"my name is {name[-1::-1]} ")


