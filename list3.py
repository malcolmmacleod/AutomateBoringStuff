def eggs(cheese):
    cheese.append('Hello')

# as  list is a reference type it is amended
spam = [1, 2 ,3]
eggs(spam)

print(spam)


## deepcopy can copy the entire list  not just the reference

>>> import copy
>>> spam = ['a', 'b', 'c', 'd']
>>> cheese = copy.deepcopy(spam)
>>> spam
['a', 'b', 'c', 'd']
>>> cheese
['a', 'b', 'c', 'd']
>>> cheese.append('e')
>>> spam
['a', 'b', 'c', 'd']
>>> cheese
['a', 'b', 'c', 'd', 'e']
>>> 

# can type lists on separate lines
>>> spam = ['apples',
...         'oranges',
...         'pears']
>>> spam
['apples', 'oranges', 'pears']

# can use line continuation character \

>>> print('this is a ' + \
... 'really long line')
this is a really long line
>>> 
