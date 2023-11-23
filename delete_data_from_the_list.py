#common methods to delete data from list
print('pop')
fruits =['apple','orange','banana','grapes']

fruits.pop() #by default last element remove
print(fruits)
fruits =['apple','orange','banana','grapes']
print(fruits.pop(1)) #whose position are one those element remove

print(fruits)

''' fruits =['apple','orange','banana','grapes']

fruits.pop(1)
fruits.pop()

print(fruits) '''
print('delete')
#delete
# same as pop methods but need to position
fruits =['apple','orange','banana','grapes']
del fruits[2]
print(fruits)
fruits =['apple','orange','banana','grapes']
del fruits[1]
print(fruits)
print()
print('remove')
# remove
# if we don't know position banana
fruits =['apple','orange','banana','grapes']
fruits.remove('banana')
print(fruits)


fruits =['apple','orange','apple','banana','grapes']
fruits.remove('apple')
print(fruits)

fruits =['apple','orange','banana','grapes']
fruits.remove('mango') #not in list
print(fruits)



