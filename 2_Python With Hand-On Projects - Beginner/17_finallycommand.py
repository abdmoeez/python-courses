num = int(input("Enter A Number: "))

try:
    print(num/0)
except:
    print("Cant divide by zero")
finally: #finally block is executed whether the error happens or not while else block runs only when error doesnot occur
    print("Code continues")