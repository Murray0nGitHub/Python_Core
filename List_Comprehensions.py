#Write a program to take a number as input, and output a list of all the numbers below that number, that are a multiple of both, 3 and 5.

#Sample Input
#42

#Sample Output
#[0, 15, 30]
#Use a list comprehension to generate the list of numbers that satisfy the condition.

x = int(input())
list = [i for i in range(x) if i % 5  == 0 and i % 3 == 0]
print(list)