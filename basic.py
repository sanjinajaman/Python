#take multiple input
''' x,y,z=input('Give me a number:').split()
print(x)
print(y)
print(z) '''



subscribes=1500
comment=1000
like=1000
if subscribes>150 and comment>100 and like>100:
    print('Awesome video')

#above the code we write this procdedure
condition=[
subscribes>150,
comment>100 ,
like>100
]
if all(condition):
    print('Awesome Video')


'''subscribes=1500
comment=1000
like=1000
if subscribes>150 or comment>100 or like>100:
    print('Awesome video')'''

#above the code we write this procdedure
subscribes=1500
comment=1000
like=1000
checkers=[
subscribes>150,
comment>100,
like>100,

]
if any(checkers):
    print('Awesome video')



subs=100
like=200
print(subs,like)

temp=subs
subs=like
like=subs

print(subs,like)
#we can swap this method

subs,like=like,subs
print(subs,like)

a=[1,2,4,2,4,5,3,3,5,3,67,3,6,4,5,67,3,3,5,63,33,5,3,4]
print(a)
#remove the duplicate
b=list(set(a))
print(b)

b=max(set(a), key=a.count)
print(b)


odd_squres=[]
for i in range(11):
    if i%2!=0:
        odd_squres.append(i**2)
print(odd_squres)

odd_squres=[i**2 for i in range(11) if i%2!=0]
print(odd_squres)



def sum(a,b):
   return a+b

res=sum(2,4)
print(res)

def sum(*a):
    result=0
    for i in a:
     result=result+i
    return result

res=sum(2,4,5,6)
print(res)


#reverse

name='sanjina jaman'[::-1]
print(name)

#palindrom
words='wow'
is_palindrom=words.find(words[::-1])==0
print(is_palindrom)