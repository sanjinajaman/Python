i=1
while i<=10:
    print(i,".sanjina")
    i=i+1

sum=0
i=1
while i<=10:
    sum=sum+i
    i=i+1
    print("sum=", sum)
   # print(sum)


n=int(input("Enter any natural number ="))
sum=0
i=1
while i<=n:
    #sum=sum+i
    sum += i
    #i=i+1
    i += 1
    print("sum=", sum)
   # print(sum)


user_input=input("Enter any number=")
sum=0
i=0
while i<len(user_input):
    sum=sum+int(user_input[i])
    i=i+1

    #print("sum",sum)
print(sum)

user_name=input("Enter Your Name:")
i=0
temp_vari=""
while i<len(user_name):
   if user_name[i] not in temp_vari:
       print(f"{user_name[i]} : {user_name.count(user_name[i])}")
       temp_vari += user_name[i]
   i+=1