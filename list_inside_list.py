matrix=[[1,2,3], [4,5,6], [7,8,9]]
# 3 items ------> 3 lists

print(matrix[0])
print(matrix[2])

'''for i in matrix:
    print(i)'''

for sublist in matrix:
    for i in sublist:
        print(i)

print(matrix[1][2])

print(type(matrix))

