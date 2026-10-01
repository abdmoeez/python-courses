num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

print("1) FOR ADDITION")
print("2) FOR MULTIPLICATION")
print("3) FOR DIVISION")
print("4) FOR SUBTRACTION")
print("5) FOR MODULAS")

choice = input("Enter your choice: ")

def add(a,b):
    print("Addition : ", a+b)
def multi(a,b):
    print("Multiplication : ", a*b)
def div(a,b):
    print("Division : ", a/b)
def sub(a,b):
    print("Subtraction : ", a-b)
def modulas(a,b):
    print("Modulas : ", a%b)


if choice =="1":
    add(num1,num2)
elif choice=="2":
    multi(num1,num2)
elif choice=="3":
    div(num1,num2)
elif choice=="4":
    sub(num1,num2)
elif choice==5:
    modulas(num1,num2)
else:
    print("Wrong choice")
