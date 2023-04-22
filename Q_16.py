#Write a program to read in numbers until the number -999 is encountered. The sum of all number read until this point should be printed out.

user_input = 0
while True:
    num = int(input("Enter a number : "))
    if num == -999:
        break
    user_input+= num
print("The sum of the numbers entered is:", user_input)