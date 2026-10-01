try:
    number = int(input("Enter a number: "))
    print(number)
except:
    print("Invalid Input")


try:
    num = int(input("Enter a number: "))
    print(num/0)
except ZeroDivisionError:
    print("Division By Zero Error")