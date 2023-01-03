#You are given the following list:
#names = ["John", "Oscar", "Jacob"]

#Complete the program to create a file where you write the names from the list, each on a new line, and separately output them.

#Output
#John
#Oscar
#Jacob
#Remember that "\n" represents a new line.

names = ["John", "Oscar", "Jacob"]

file = open("names.txt", "w+")

for i in names:
    file.write(i + "\n")
file.close()

file= open("names.txt", "r")
print(file.read())


file.close()

