# in keyword and iterations in dictionary
user_info={
    'name':'sanjina jaman',
    'age':'19',
    'faculty':"cse",
    'id':"1935202505",
    'batch':'52',
    'names':['sanjina','sinchu','bintu']
    }
#check if  key exist in dictionary
if 'name' in user_info:
    print('present')
else:
    print('not present')

# check if value exist in dictionary----> values method

if 'sanjina jaman' in user_info.values():
    print('present')
else:
    print('not present')

# check if list type value  exist in dictionary ----> values method
if ['sanjina','sinchu','bintu'] in user_info.values():
    print('present')
else:
    print('not present')


#loops in dictionaries

for i in user_info:
    print(i)



for i in user_info.values():
    print(i)


#values method

user_info_values=user_info.values()
print(user_info_values)
print(type(user_info_values))


#keys method
user_info_keys=user_info.keys()
print(user_info_keys)
print(type(user_info_keys))



#loops in dictionaries

for i in user_info:
    print(user_info[i])
# items method
user_info_items=user_info.items()
print(user_info_items)
print(type(user_info_items))

# another items method using loop
for key,value in user_info.items():
    print(f'key is {key},and value is {value}')

#another
for i,j in user_info.items():
    print(f'key is {i},and value is {j}')
