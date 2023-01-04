#Sets are created using curly braces and they hold unique values.

#Given two sets, find and output all the elements that are common to both sets.
#For example, for the following sets:
#{'a', 'b', 'c'}
#{'c', 'd', 'e'}

#The output should be {'c'}, as it is present in both sets.
#The output should be a set, containing the common elements.

set1 = {2, 4, 5, 6}
set2 = {4, 6, 7, 8, 11, 42, 2}

print(set1 & set2)