mydict = {"name":"Max" , "age":28 , "city":"New York"}
print(mydict)

if "name" in mydict:
    print(mydict["name"])

#############

try:
    print(mydict["last"])
except:
    print("Error")

##############

#Looping 

for key,value in mydict.items():
    print(key,value)


