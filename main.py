mixed=[3,4,5,6,"three","four","five","six"]

print(mixed)

mixed[1:]="two"
print(mixed)
mixed[:]=[1,2,3,4,5,6,7,8,]
print(mixed)
mixed[:]=[9,2,3,4,5,6,7,8,]
mixed[:1]=[1]
print(mixed)

# add to list
subject=[]
subject.append('dld')
subject.append('dbms')
subject.append('os')
print(subject)

subject=['dld','dbms','os']
subject.insert(0,"stastitics & probability")
print(subject)


job1=['job1','job2','job3']
job2=['job4','job5','job6']
job=job1+job2
print(job)


job1.extend(job2) #add string
print(job1)
print(job2)
job1.append(job2) #list inside another list