file = open("employees.txt","r")

print(file.readable()) #readable funtion tells whether a file is readable or not using boolean

print(file.read()) #Reads whole file

print(file.readlines())

file.close()