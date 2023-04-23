#20. Write a program to find the sum of cubes of first n numbers (using for loop).

n = int(input("Enter a positive integer n: "))

sum_of_cubes = 0

for i in range(1, n+1):
    sum_of_cubes += i**3

print("The sum of cubes of the first", n, "natural numbers is:", sum_of_cubes)
