#tuples are immutable
#tuples are ordered collections of items
#tuples can store any data type
#you cannot change (add or delete)values from tuple once it created
#but can add,delete data from list which is present inside tuples
# something more about tuples,list, string

#mixed=(1,2,3,4,"five",[1,2,3])
#no append, no pop, no insert, no remove
#only count and index
#looping in tuples
#tuple with one element
#tuple without parenthesis
#tuple unpacking
#list inside tuple
#some functions that you can use with tuples

print('looping in tuples')
numbers=(1,2,3,4,5)
for i in numbers:
    print(i)


print('count')
def count_item(l):
    count=0
    for i in l:
        if type(i)==list:
            count +=1
    return count

mixed=(1,2,3,4,"five",[1,2,3],[1,2,3])
print(count_item(mixed))
#list inside tuple
print('index')
poped_value=mixed[5].pop()
print(poped_value)
mixed=(1,2,3,4,"five",[1,2,3])

print(mixed.index(3))
#mixed[2].append(2)
#mixed[0].append(1)
#functions
print('tuple with one element')

tuples=(1,)
print(tuples)
print(type(tuples))

print('min(),max(),len(),sum()')
nums=(1, 2, 3, 4, 5, 6, 7, 8, 9)
print(max(nums))
print(min(nums))
print(len(nums))
print(sum(nums))
print('create tuples')
numbers=tuple(range(1,10))
print(numbers)
print('tuple without parenthesis')
without_parenthesis=1,2,3,4,5
print(without_parenthesis)
print(type(without_parenthesis))

print('tuple unpacking')
numbers=(1,2,3)
one,two,three=numbers
print(one)

nums=(1, 2, 3, 4, 5, 6, 7, 8, 9)
print(list(nums))


nums=(1, 2, 3, 4, 5, 6, 7, 8, 9)
strings=str(nums)
print(strings) # this output look like (1, 2, 3, 4, 5, 6, 7, 8, 9) as like tuples but it's not tuples ,it's string we print it's data type next line
print(type(strings))
