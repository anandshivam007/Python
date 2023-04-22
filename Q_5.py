##5 Given as input a floating (real) number of centimeters, print out the equivalent
##number of feet (integer) and inches (floating, 1 decimal), 
# with the inches given to an accuracy of one decimal place. Assume 2.54 centimeters per inch, and 12 inches per foot.


cm = float(input("Enter the Number in cm"))
feet = int((cm/30.48))
inch = round((cm/2.54),1)
print(feet)
print(inch)

