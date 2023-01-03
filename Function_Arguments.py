#You are given a program with two inputs: one as password and the second one as password repeat. Complete and call the given function to output "Correct" if password and repeat are equal, and output "Wrong", if they are not.

#Sample Input
#nfs1598
#nfs1598

#Sample Output
#Correct
#Don't forget to add arguments when you call the function.

password = input()
repeat = input()

def validate(text1, text2):
	if text1==text2:
		print("Correct")
	else:
		print("Wrong")
validate(password,repeat)

