#Write a program to find out the sum of squares of n numbers.

n = int(input("Enter the number till you want the sum of squares: "))

sum_of_squares = int(n*(n+1)*(2*n+1)/6)
print(sum_of_squares)