#function returning two values as a tuples

def func(value1,value2):
    add=value1+value2
    multiply=value1*value2

    return add,multiply

print(func(2,3))#return output as a tuples
add,multiply=func(5,6)
print('Add=',add)
print('Multiply',multiply)
