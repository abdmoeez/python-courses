###########
#merging dictionaries

dict1 = {"name": "Max","age":28 ,"email":"max@xyz.com"}
dict2 = dict(name = "Mary", age=27, city="Boston")

dict1.update(dict2) #updates the values and adds the new keys

print(dict1)