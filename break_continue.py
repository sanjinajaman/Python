# print 1 to n
n = int(input("Enter your number:"))
i = 0
for i in range(n + 1):
    if i == 11:
        break
    print(i)
# print 1 to 10 but not print 5

for i in range(1, 11):
    if i == 5:
        continue
    print(i)
