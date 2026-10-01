name = "root admin user ROOT USER root"

print(len(name))
print(len("admin"))
print(name.upper())
print(name.lower())
print(name.capitalize()) #Capitalize first element of string
print(name.title()) #Capitalizes first element of each word
print(name.replace("root","dimalu"))
replaced_value = name.replace("root","dimalu")
print(replaced_value)
print(name.count("root"))

url = "https://www.google.com"
print(url)
print(url[8:]) #through Slicing we can skip certain number of elements and print only required 
print(url[:-4]) #slices from right side