#We have a function that outputs "Welcome, user" as it is called. We want to make it more personalized, so redesign the given function so that it will take the given input as the name of the user and output the welcome message with it.

#Sample Input
#Tommy

#Sample Output
#Welcome, Tommy
#Don't forget to call the function.

def welcome_message():
	name = input()
	print("Welcome, " + name)

welcome_message()