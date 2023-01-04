#All the products in online shop have their own ID. Every ID consists of 4 symbols:
#The first symbol: an uppercase character
#The second symbol: an uppercase character
#The third symbol: a digit
#The forth symbol: a digit

#Write a program for a search tool, that will take the ID as input and output "Searching" if the format is correct, and "Wrong format", if it's not.

#Sample Input
#LG17

#Sample Output
#Searching
#Remember to use $ sign in pattern to set the ending of the ID string.


import re
id = input()

if re.search(r"[A-Z][A-Z][0-9][0-9]$", id):
    print("Searching")
else:
    print("Wrong format")