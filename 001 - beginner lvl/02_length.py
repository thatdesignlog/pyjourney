# from https://github.com/bregman-arie/python-exercises/blob/main/exercises/hello_world/length.md
# exercise was tested with https://www.online-python.com/

# question list:
# How to print the length of the string 'abcd' ?
# How to print the length of the variable x (x is the list [5, 30 ,2]) ?
# What would be the length of following dictionary {'x': 3, 'y': 3} ?
# What would be the length of the tuple ('x', 'y') ?

--------

# 01. how to print length of string 'abcd'?

meovv = 'abcd'
print(len(meovv))

# 02. how to print length of the variable x if x is the list of [5,30,2]?

x = [5, 30, 2]
print(len(x))

# 03. what would be the length of following dictionary {'x': 3, 'y':3}?

random_dictionary =  {
  'x': 3,
  'y': 3,
}

print(len(random_dictionary))

# 04. What would be the length of the tuple ('x', 'y')

random_tuple = ('x', 'y')
print(len(random_tuple))


# note: there is no solution from the python repo, so these are all my answers
# dev-reflection: there are some parts that i didn't know but i went to w3 to find resources and tested them with an online IDE before putting in my answers. 
# dictionary in python seems to have a similar functionality as dictionary in c#. that was my first time learning about a 'tuple'. 
# now i know how to differentiate list, set, dictionary, and tuple. a tuple uses () and ordered like a list but a tuple is unchangable & a list is changeable. 
# both tuple & list allow duplication. a set & a dictionary both use {} for their collection and both don't allow duplication. dictionary has {'something': 'another something'}
# whereas a set is singular item. Once a set is created, you cannot change its items, but you can remove items and add new items. 
# Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

# resources: 
# a tuple - https://www.w3schools.com/python/python_tuples.asp
# a dictionary - https://www.w3schools.com/python/python_dictionaries.asp


