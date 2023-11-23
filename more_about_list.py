#generate lists with range function
#index method
#pass list to a function

numbers=list(range(1,12))

print(numbers)
print(numbers.index(7))
t=numbers.index(6)
print(t)
print(numbers)

numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9,1, 10, 11]

print(numbers.index(1,3))
print("function")
numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9,1, 10, 11]
def negative_list(l):
    negative=[]
    for i in l:
      negative.append(-i)
    return negative
print(negative_list(numbers))


print("ex-1(5)")
numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9,1, 10, 11]
def lists (l):
    x=[]
    for i in l:
        x.append(i**2)
    return x
print(lists(numbers))


def lists_square(l):
    squre=[]
    for i in l:
        squre.append(i**2)
    return squre
number= list(range(1,11))
print(lists_square(number))






