#8.write a program to find the biggest of 3 numbers
num1 = int(input("Enter the First number: "))
num2 = int(input("Enter the Second number: "))
num3 = int(input("Enter the Third number: "))
if num1 > num2 and num1 > num3:
 print(f"{num1} is greatest")
elif num2>num1 and num2 > num3:
 print(f"{num2} is greatest")
else :
 print(f"{num3} is greatest")
