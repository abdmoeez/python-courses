num = int(input("Enter A Number: "))

try:
    print(num/0)
except:
    print("Cant divide by zero")


try:
    print(num/0)
except ZeroDivisionError as e:
    print(e)