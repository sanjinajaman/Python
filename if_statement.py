# age=int(input("Enter your age:"))
# if age>14:
#     print("Your age is  ",age)
# elif age==14:
#     print("Your age is ",age)
# else:
#     print("error")
#
# print("Short Hand If")
# a=int(input("Enter number:"))
# b=int(input("Enter number:"))
# if a > b:print("a is greater than b")
# elif a<b:print("b is greater than a")
# elif a == b:print("a is equal to b")
# else:print("error")


# print("**********AND****************")
# num1=int(input("Enter num1="))
# num2=int(input("Enter num2="))
# num3=int(input("Enter num3="))
# if num1>num2 and num1>num3:
#     print("num1 is greater than num2 and num3")
# elif num1<num2 and num1<num3:
#     print("num is less than num2 and num 3 ")
#
#
#
# print("**********OR****************")
# num1=int(input("Enter num1="))
# num2=int(input("Enter num2="))
# num3=int(input("Enter num3="))
# if num1>num2 or num1>num3:
#     print("num1 is greater than num2 and num3")
# elif num1<num2 or num1<num3:
#     print("num is less than num2 and num 3 ")


# print("******NESTED IF*********")
# num=9
# if num>10:
#     print("Above ten")
#     if num>20:
#         print("And also above 20")
#     else:print("not above 20")
# else:print("Below 10")

# print("EX")
# winning_number=int(input("Enter any number: "))
# guss_num=int(input("Guss a number:"))
# if winning_number==guss_num:
#     print("YOU WIN!!!")
# elif winning_number<guss_num:
#     print("too low")
# elif winning_number>guss_num:
#     print("too high")
# print("ex")
# winning_number = int(input("Enter any number: "))
# guss_num = int(input("Guss a number:"))
# if winning_number == guss_num:
#    print("YOU WIN!!!")
# else:
#     if winning_number < guss_num:
#         print("too low")
#     else:
#         print("too high")
#






# print("and operation")
# name=input("Enter your name")
# age=int(input("Enter Your age"))
# if (name[0]=="a" or name[0]=='A') and age>10:
#     print("You can watch coco movie")
# else:
#     print("You can't watch coco movie")






# #pass statement
# x=10
# if x>9:
#     pass #pass is a null statement



# print("Ex")
#
# age=int(input("Enter Your Age:"))
# if age==1 or age<=3:
#     print("free")
# elif age==4 or age<=10:
#     print("150")
# elif age == 11 or age <=60:
#     print("250")
# elif age >60:
#     print("200")


print("Ex")

age=int(input("Enter Your Age:"))
if  0<age<=3:
    print("Your tiket price: free")
elif 3<age<=10:
    print("Your tiket price:150")
elif 10<age <=60:
    print("Your tiket price:250")
elif age >60:
    print("Your tiket price:200")