#Write a program to read 10 numbers and compute the sum of even numbers and
#sum of odd numbers

even_sum = 0
odd_sum = 0
num_count = 0
while True:
    num = int(input("Enter a number : "))
    if num_count == 9:
        break
    num_count+=1
    if num % 2 ==0:
        even_sum+=num
    if num % 2 != 0:
        odd_sum+=num
print(even_sum)
print(odd_sum)