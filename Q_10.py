##10.Input student marks in 5 subjects and find out the sum, average and based on
##the average give them grading as follows:
##i. Average > 60 I Division
##ii. Average > 50 II Division
##iii. Average > 40 III Division
##iv. Average < 40 Fail
sub1 = int(input("Enter the marks is Hindi : "))
sub2 = int(input("Enter the marks is English : "))
sub3 = int(input("Enter the marks is Science : "))
sub4 = int(input("Enter the marks is Maths : "))
sub5 = int(input("Enter the marks is SST : "))
sum = sub1+sub2+sub3+sub4+sub5
avg = int(sum/5)
if avg > 60 :
 print("You have secured first Division")
elif avg > 50 and avg <= 60 :
 print("You have secured second Division")
elif avg > 40 and avg <= 50 :
 print("You have secured third Division")
elif avg < 40 :
 print("You have Failed")