print("...Calculator...")

num1= float(input("Enter a number: "))
num2= float(input("Enter another number: "))

print("1.Addition\n2.Substraction\n3.Multiplication\n4.Division")

choice=int(input("Enter your choice(1-4): "))

if choice==1:
    print("Addition of both the numbers: ",num1+num2)
elif choice==2:
    print("Substraction of the numbers: ",num1-num2)
elif choice==3:
    print("Multiplication of the numbers: ",num1*num2)
elif choice==4:
    print("Division of the numbers: ",num1/num2)
else:
    print("Invalid input")