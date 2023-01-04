#Given text as input, output the number of words it contains.

#Sample Input
#hello world

#Sample Output
#2
#The split() method can be used to split the string into words.


txt = input()

words = txt.split(" ")
print(len(words))