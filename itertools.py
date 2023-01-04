#You are given a list of items, and need to find all the possible orders of the items.
#The output should be a list, containing all possible orders.

#Sample Input
#['a', 'b']

#Sample Output
#[('a', 'b'), ('b', 'a')]
#The itertools module contains many useful functions that can achieve the above mentioned task.

from itertools import permutations

items = ['x', 'y']

result = list(permutations(items))
print(result)