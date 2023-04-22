##13.In a company worker efficiency is determined on the basis of time required for a
##worker to complete the job. If the time taken by the worker is 2 – 3 hrs, then
##the worker is said to be highly efficient (STAR). If the time required by worker is
##3 – 4 hrs, then the worker is ordered to improve speed (MERITORIUS). If the
##time taken is between 4 – 5 hrs, the worker is given training to improve speed
##(ADEQUATE), and if the time taken by the worker is more than 5 hours, then
##the worker has to leave the company (TRAILER). If the time taken by the
##worker is input through the keyboard, find the efficiency of the worker.


time_taken = int(input("Enter the time taken by the worker : "))
if time_taken > 2 and time_taken <= 3 :
 print("Worker is highly efficient (STAR)")
elif time_taken > 3 and time_taken <= 4 :
 print("Worker should improve his speed (MERITORIUS)")
elif time_taken > 4 and time_taken <= 5 :
 print("Worker should leave the company (ADEQUATE)")
elif time_taken > 5 :
 print("Worker should leave the company (TRAILER)")