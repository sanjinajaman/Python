#funtion

name="sanjina"
print(len(name)) #here len is a function but it is built in function
def add_two_num(a,b):
    return a+b

a=int(input('Enter first number' ))
b=int (input('Enter second number'))
total=add_two_num(a,b)
print('total=',total)


a=float(input('Enter first number' ))
b=float (input('Enter second number'))
total=add_two_num(a,b)
print('total=',total)




def add_two_string(a, b):
    return a+ b

a=input('Enter first name' )
b=input('Enter last name')
total_String=add_two_string(a, b)
print(total_String)



#function Practice


def last_char(name):
    return name[-1]

name="sanjina"
print(last_char(name))
#print(last_char(9))#type error


#check odd even
def odd_even(a):
    if a%2==0:
        print("Even")
    else:
        print("odd")

a=int(input('Enter any number='))
odd_even(a)


#check odd even
# def odd_even(a):
#     if a%2==0:
#         return "Even"
#     else:
#         return "odd"

def odd_even(a):
     if a%2==0:
         return "Even"
     return "odd"

a=int(input('Enter any number='))
print(odd_even(a))

def is_even(a):
    if a%2==0:
        return True
    else:
        return False
print(is_even(2))

#reduce same code
def is_even(a):
    if a%2==0:
        return True
    return False
print(is_even(3))



def is_even(a): #here a is perameter
     return a%2==0 #True

print(is_even(3)) #here 3 is argument


def song():
    return "aj khub megh koruk"
print(song())



# check greater than

def greatest(a,b):
     if a>b:
         print(a,'is greater than b')
     else:
         print(b," is greater than a")

a= int(input("Enter any number="))
b= int (input('Enter any number='))
greatest(a,b)



# check greater than

def greatest(a,b,c):
     if a>b and a>c:
         return a
     elif b>a and b>c:
           return b
     elif c>a and c>b:
         return c

a= int(input("Enter any number="))
b= int (input('Enter any number='))
c= int (input('Enter any number='))

biggest=greatest(a,b,c)

print(f'{biggest} is greater')



def greater(a, b):
    if a > b:
        return a
    else:
        return b



# check greater than

def new_greatest(a,b,c):
     # biggest=greater(a,b)
     # return greater(biggest,c)
     return greater(greater(a,b),c)
a= int(input("Enter any number="))
b= int (input('Enter any number='))
c= int (input('Enter any number='))

print(new_greatest(a,b,c))

#big=new_greatest(a,b,c)

#print(f'{big} is greater')