
>>> myCat = ['size': 'fat', 'colour': 'grey', 'disposition': 'loud']
  File "<stdin>", line 1
    myCat = ['size': 'fat', 'colour': 'grey', 'disposition': 'loud']
                   ^
SyntaxError: invalid syntax
>>> myCat = {'size': 'fat', 'colour': 'grey', 'disposition': 'loud'}
>>> myCat
{'size': 'fat', 'colour': 'grey', 'disposition': 'loud'}
>>> spam = {12345: 'Luggage combination', 42" 'answer'}
  File "<stdin>", line 1
    spam = {12345: 'Luggage combination', 42" 'answer'}
                                                      ^
SyntaxError: EOL while scanning string literal
>>> spam = {12345: 'Luggage combination', 42: 'answer'}
>>> print ('My cat is ' + myCat['size'])
My cat is fat
>>> # dictionaries have no order
>>> 
>>> # accessing  a key that is not in a dictionary results in a key error
>>> myCat['age']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'age'
>>> # you can check if a dictionary has a key with the in operator
>>> 'size' in myCat
True
>>> 'age' in myCat
False
>>> # to get keys in a dictionary:
>>> myCat.keys()
dict_keys(['size', 'colour', 'disposition'])
>>> # to get values in a dictionary
>>> myCat.values()
dict_values(['fat', 'grey', 'loud'])
>>> # to get a list of items in a dictionary
>>> myCat.items()
dict_items([('size', 'fat'), ('colour', 'grey'), ('disposition', 'loud')])
>>> # can iterate around this
>>> for k in myCat.keys()
  File "<stdin>", line 1
    for k in myCat.keys()
                        ^
SyntaxError: invalid syntax
>>> for k in myCat.keys():
...     print (k)
... 
size
colour
disposition
>>> # items returns tuples
>>> for k, v in myCat.items():
...     print k
  File "<stdin>", line 2
    print k
          ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(k)?
>>>     print(k)
  File "<stdin>", line 1
    print(k)
    ^
IndentationError: unexpected indent
>>> for k, v in myCat.items():
...     print(k)
...     print(v)
... 
size
fat
colour
grey
disposition
loud
>>> # there is a get method
>>> # which returns a default value if the key does not exist
>>> myCat.get('size', 'normal')
'fat'
>>> myCat.get('age', 42)
42
>>> # the setDefault methos sets a value in a dictionary only if the key doesn't already exist
>>> myCat,setDr
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'setDr' is not defined
>>> myCat.setDefault('age', 42)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'dict' object has no attribute 'setDefault'
>>> myCat.setdefault('age', 42)
42
>>> myCat
{'size': 'fat', 'colour': 'grey', 'disposition': 'loud', 'age': 42}
