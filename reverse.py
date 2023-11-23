#define a function which will take list as a argument and this function will return a reversed list

#example
#[1,2,3,4,5]------>[5,4,3,2,1]
#['word1','word2','word3']----['word3','word2','word1']
print("using pop_append")
def reverse_list(list):
    reverse=[]
    for i in range(len(list)):
        poped_value=list.pop()
        reverse.append(poped_value)
    return reverse


numbers=[1, 2, 3, 4, 5]
print(len(numbers))
print(reverse_list(numbers))

print("using reverse method")
def reverse_list(list):
      list.reverse()
      return list

numbers=[1, 2, 3, 4, 5]
print(len(numbers))
print(reverse_list(numbers))


print("using slicing method")
def reverse_list(list):
      return list[::-1]

numbers=[1, 2, 3, 4, 5]
print(len(numbers))
print(reverse_list(numbers))


'''def reverse_list(l):
    reverse=[]
    for sublist in l:
        for i in sublist:
            #print(i)
           poped_value=sublist.pop()
           reverse.append(poped_value)
    return reverse


list=['abc','xyz']
print(reverse_list(list))'''


def reverse_list(l):
    reverse=[]
    for i in l:
        reverse.append(i[::-1])
    return reverse


list=['abc','xyz']
print(reverse_list(list))