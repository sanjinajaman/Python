#compare list
# == , is

fruits1=['apple','mango','apple','orange']
fruits3=['apple','mango','apple','orange']
fruits2=['banana','grapes','guava','orange']

print(fruits1==fruits2)

print(fruits1==fruits3)#check value ....values are same ....then output show true

print(fruits1 is fruits3) # check those list memory are ase or not.....output false


def compare(l1,l2):
    new_list = []
    for i in l1:
        if i in l2:
           new_list.append(i)
    return  new_list

list1=[1,3,4,9,]
list2=[1,2,3,4]
print(compare(list1,list2))