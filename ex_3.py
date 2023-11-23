name,char=input("enter your name and enter a character:").split(",")
print(f"length of your name is {len(name)}")
print(f"character count:{name.count(char)}") #case sensitive
#name=name.lower()
#char=char.lower()

print(f"character count:{name.lower().count(char.lower().strip())}") #case  insensitive
