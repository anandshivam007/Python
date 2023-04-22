#9. write a program to input 3 numbers and arrange them in ascending order
num = []

for i in range(3):
    number = int(input("Enter the number "))
    num.append(number)
num.sort()
print(num)