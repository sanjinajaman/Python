user_info={
    'name':'sanjina jaman',
    'age':20,
    'id':'1935202505',
    'faculty':'cse',
    'batch':'52'

}

#how to add data
user_info['fav_songs']=['song1','song2','song3']
print(user_info)

#pop method
poped_item=user_info.pop('batch')#without argument show error
print(f'poped item is {poped_item}')
print(user_info)

#pop item method
poped_item=user_info.popitem()
print(user_info)
print(poped_item)

print(type(poped_item))
