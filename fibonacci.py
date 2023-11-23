#fibonacci series

# 0 1 1 2 3 5 8 13 21

# 1--------> 0
# 2--------> 0 1
# 3--------> 0 1 1
# 4--------> 0 1 1 2
# 5--------> 0 1 1 2 3
# 6--------> 0 1 1 2 3 5


for i in range(1,11):
    #print(i)

    print(i , end=" ")

    #print(i, end="\n")

def fibonacci_seq(n):
    a=0 #first number fibonacci series
    b=1 #second number fibonacci series
    if n==1:
        print(a)
    elif n==2:
        print(a,b)
    else:
        print(a,b, end=" ")
        for i in range(n-2):
            c=a+b
            a=b
            b=c
            print(b,end=" ")

n=int(input('Enter any number='))
fibonacci_seq(n)

