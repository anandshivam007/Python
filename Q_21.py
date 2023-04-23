# 21. Write a program to count the vowels and letters in free text given as standard
# input. Read text a character at a time until you encounter end-of-data. Then
# print out the number of occurrences of each of the vowels a, e, i, o and u in the
# text, the total number of letters, and each of the vowels as an integer
# percentage of the letter total. Suggested output format is: Numbers of characters:
# a 3 ; e 2 ; i 0 ; o 1 ; u 0 ; rest 17

lst = []
rest = 0
str = input("Enter the text: ").lower()
lst = (list(str))
for i in lst:
    if(i == 'a'or i == 'e'or i == 'i'or i == 'o'or i == 'u' or
        i == 'A'or i == 'E'or i == 'I'or i == 'O'or i == 'U' ):
        print("a: ",lst.count('a'))
        print("e: ",lst.count('e'))
        print("i: ",lst.count('i'))
        print("o: ",lst.count('o'))
        print("u: ",lst.count('u'))
    elif i.isalpha():  
        rest+=1
print("rest: ",rest)

