#Write a program to control entrance to a club.
#Only people who are 18 or older are allowed to enter the club.
#The given program takes the age and the name of the person who tries to enter.
#Complete the program to output "Welcome" followed by the name of the person if they are allowed to enter the club, and "Sorry" if they are younger than the allowed age.

#Sample Input
#24
#James

#Sample Output
#Welcome James
#Do not forget to put a space between "Welcome" and the name.

age = int(input())
name = input()
if age >= 18:
	print("Welcome" + " " + name)
else:
	print("Sorry")