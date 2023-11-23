# filter odd even
#difine function


def odd_even(l):
    even=[]
    odd=[]
    for i in l:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    output=[even,odd]
    return output

list = [1, 2, 3, 4, 5]
print(odd_even(list))