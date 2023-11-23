
def no_item(l):
    count=0
    for i in l:
        if type(i)==list:
            count +=1
    return count


numbers=[ [1,2,3],[2,3,4,5],[3,3,4,5]]
print(no_item(numbers))

print(type(numbers))