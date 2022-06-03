lists = [1,2,3,344,33,4,43,5,6,6,7,7,11,1,2,3]
# using the set builit-in function to remove duplicates in python
uniquevalues = set(lists)
print('Removing the duplicates in the list using set function')
print(uniquevalues)

# we can convert set to list

uniquevalues_list = list(uniquevalues)
print("After removing the duplicate in the list")

print("set to list convertion : ",uniquevalues_list)



s = 'ab cd:ef gh'
s.split(' ')  # ['ab', 'cd:ef', 'gh']
s.split(':')  # ['ab cd', 'ef gh']

#Q: Can we split on either ' ' or ':'?
# A: Not with str.split, but re.split can:

import re
print("Spiliting the string using regular expressions")
print(re.split('[: ]', s))  # ['ab', 'cd', 'ef', 'gh']
