name="          sanjina           "
star="*****"
#strip method removes space
#left side space remove lstrip method

print(name+star)
print(name.lstrip()+star)
print(name.rstrip()+star)
print("Your name is:",name.lstrip()+star)
print("Your name is:",name.rstrip()+star)#right side space remove rstrip method
print("Your name is:",name.strip()+star)


name="san        jina"
print(name)
print(name.strip()) #strip method can't solve it
print(name.replace(" ",""))


