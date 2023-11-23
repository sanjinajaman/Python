same={
    'name':'unknown',
    'age':'unknown',
    'height':'unknown'
}

print(same)

same=dict.fromkeys(['name','age','height'],'unknown')
print(same)
same1=dict.fromkeys(('name','age','height'),'unknown')
print(same1)
same2=dict.fromkeys('nameageheight','unknown')

print(same2)

same3=dict.fromkeys(range(1,11),'unknown')
print(same3)

same4=dict.fromkeys(['name','age','height'],['unknown','unknown'])
print(same4)

#get method(useful)


same={
    'name':'sanjina',
    'age':'unknown',
    'height':'unknown'
}
print(same['name'])

print(same.get('name'))#for key access better use get method

#print(same['names'])
print(same.get('names'))


if 'name' in same:
    print('present')
else:
    print('not present')

if same.get('names'):
    print('present')
else:
    print('not present')
#clear method
'''same.clear()
print(same)
print(same.clear())
clear=same.clear()
print(clear)'''

print('copy method')
copy2=same.copy()
print(copy2)
copy2=same
print(copy2.popitem())
print(same)

print(copy2==same)



