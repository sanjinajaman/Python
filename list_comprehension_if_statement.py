#list comprehension with if statement
numbers=list(range(1,11))
print(numbers)
nums=[]
num=[]
for i in numbers:
    if i%2==0:
        nums.append(i)
print(nums)


#comprehension with if statement

even_numbers=[i for i in numbers if i%2==0]
print(even_numbers)
even_num=[i for i in range(1,11) if i%2==0]
print(even_num)
odd_num=[i for i in numbers if i%2!=0]
print(odd_num)
print('enter ')

def num_to_string(l):
      return [str(i) for i in l if (type(i)==int or type(i)==float)]


l=['True','False',1,1.2,3]
print(num_to_string(l))
