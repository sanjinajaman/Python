print("***********STRING METHODS************")
name="sanjina"
length=len(name) #length 7
print(length)

name="sanjina Jaman"
length=len(name) #length 13
print(length)

print(name.lower())
print(name.upper())
print(name.title())
print(name.count("a"))

print("********replace******")
text="I like banana"
print(text)
print(text.replace("banana","apple")) #string.replace(oldvalue, newvalue, count)

text=" one one one one"
print(text)

print(text.replace("one","two"))
print(text.replace("one","two",2)) #string.replace(oldvalue, newvalue, count)

print("********find******")
text1=" one one one"
text2="one one one"
print(text1.find("one"))
print(text2.find("one"))
print(text2.find("one",1))#string.find(value, start, end)


text1="one one one"

one_pos=text1.find("one")
one_pos2=text1.find("one",one_pos+1)
print(one_pos)
print(one_pos2)
print(text1.replace("one_pos2","two",2))


print("********center**************")
string="python is awesome"
print(string.center(len(string)+4,"*")) #string.center(length, character)
string="string are immutable"
print(string[5])
#string[5]='T' #error
#print(string[5])

new_string=string.replace("t","T",2)

print(new_string)
print(string)


name='sanji'
name=name+'na'
print(name)

name1="sanji"
name1+='na'
print(name1)












