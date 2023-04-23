#Write a program to find out the factorial of a given number

num = int(input("Enter the number for which factorial has to b calculated : "))

factorial = 1

if num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)