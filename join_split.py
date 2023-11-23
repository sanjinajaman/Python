# split method
# convert string to list
# join method
# convert list to string

x='sanjina jaman sinchu'
y='sanjina,jaman,sinchu'
name, age =input('enter your name and age').split(',')
print(name,age)
print(age)
print(y.split(','))
print(x.split()) # using split method we convert list from string
print(x)
# convert list to string
fruits=['apple','mango','orange']
print((',').join(fruits))