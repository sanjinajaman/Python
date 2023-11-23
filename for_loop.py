#sum of 1 to 10
i=4
sum=0
for i in range(1,11):
    sum+=i
print(sum)
#user input
# user_input=int(input("Enter any number:"))
# sum=0
# for i in range(1,user_input+1):
#     sum+=i
# print(sum)


# num=input("Enter any number")
# sum=0
# for i in range(len(num)):
#     sum+=int(num[i])
#     print(sum)

name=input("Enter your name")
temp_vari=""
i=0
for i in range(len(name)):
    if name[i] not in temp_vari:
     print(f"{name[i]}: {name.count(name[i])}")
     temp_vari+=name[i]