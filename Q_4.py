#4.Write a program to read a "float" representing a number of degrees Fahrenheit,and print as a "float" the equivalent temperature in degrees Celsius. 
#Print your results in a form such as 212.0 degrees Fahrenheit converts to 100.0 degrees Celsius.

farenheit = float(input("Enter the temperature in Farenheit: "))
celsius = float(5*(farenheit-32)/9)
print("Temperature in celsius is",celsius)

