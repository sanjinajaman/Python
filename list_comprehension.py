#list comprehension
#with the help of list comprehension we can create of list in one line

#create a list of squares from 1 to 10
#list comprehension means creat list in one line
squares_list=[]

for i in range(1,11):
    squares_list.append(i**2)
print(squares_list)

squares_list2=[ i**2 for i in range(1,11)]
print(squares_list2)

squares_list1=[]
for i in range(1,11):
    squares_list1.append(-i)
print(squares_list1)


squares_list3=[ -i for i in range(1,11)]
print(squares_list3)


names_list=['sanjina','sinchu','bintu']

new_name_list=[]

for name in names_list:
    new_name_list.append(name[0])
print(new_name_list)


names_list1=['sanjina','sinchu','bintu','jaman']

new_name_list1=[name[0] for name in names_list1]
print(new_name_list1)

list=['abc','tuv','xyz']
new_list=[]
for i in list:
    new_list.append(i[::-1])
print(new_list)

list1=['abc','tuv', 'xyz']

new_list1=[i[::-1] for i in list1]
print("list1=",new_list1)
