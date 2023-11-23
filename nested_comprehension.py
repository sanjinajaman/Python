lists=[[1,2,3],[1,2,3],[1,2,3]]
nested_comprehension=[[i for i in range(1,4)]  for i in range(1,4)]
print(nested_comprehension)

nested_comprehension=[[i for i in range(1,4)]  for j in range(1,4)]
print(nested_comprehension)



new_list=[]
for i in range(3):
    new_list.append([1,2,3])
print(new_list)