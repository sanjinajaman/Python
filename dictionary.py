# what are dictionary?
#unordered collections of data in key : value pair
print('how to create dictionaries')
identy={
    "name":"sanjina",
    "id" :"1935202505",
    "batch":"52",
    'department':'cse'
}

print(identy)

print(identy["name"])

print(identy["department"])

print('2nd method to create dictionary')
identy=dict(name ='sanjina',id='1935202505')
print(identy)

print("=====length of Dictionary=====")
print(len(identy))


print("=====not allowed  of duplicate variable =====")
sanjina={
    "name":"sanjina",
    "id" :"1935202505",
    "batch":"52",
    #"batch":"52",
    'department':'cse'
}
print(sanjina)
print(type(sanjina))

sanjina={
    "name":"sanjina",
    "id" :"1935202505",
    "batch":"52",
    #"batch":"52",
    'department':'cse'
}
print(sanjina)
print('how to access data from dictionary')
# there is no indexing because of unordered collections of data
print(identy['name'])
print(identy['id'])

#which type of data a dictionary can store
#anything
#list, strings,dictionary,numbers

user_info={
    'name':"sanjina",
    'id':['1935202505']
}
print(user_info)
print(user_info['id'])
print('how to add data to empty dectionary')
user_info2={}

user_info2['name']='sanjina'
user_info2['age']=19
print(user_info2)


