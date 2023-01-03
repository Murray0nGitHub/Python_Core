#You have a magic box that doubles the count of items you put, in every day.
#The given program takes the initial count of the items and the number of days as input.

#Task
#Write a program to calculate and output items' count on the last day.

#Sample Input
#3
#2

#Sample Output
#12

#Explanation
#Day 1: 6 (3*2)
#Day 2: 12 (6*2)
#Use *= operator to multiply the count of the items by 2 in each iteration.

items = int(input())
days = int(input())
while days>0:
	items*=2
	days-=1
print(items)