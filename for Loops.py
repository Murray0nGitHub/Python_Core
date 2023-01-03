#for loops allow you to easily iterate through lists.

#Given a list of numbers, output their sum.

#Sample Input
#1 3 7 5

#Sample Output
#16
#Output the sum after the loop.

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

sum = 0
for num in list:
    sum+=num
print(sum)