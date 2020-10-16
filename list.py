
>>> ['Cat', 'Bat', 'Rat', 'Elephant']
['Cat', 'Bat', 'Rat', 'Elephant']
>>> spam = ['Cat', 'Bat', 'Rat', 'Elephant']
>>> spam
['Cat', 'Bat', 'Rat', 'Elephant']
>>> spam[0]
'Cat'
>>> spam[1]
'Bat'
>>> spam[-1]
'Elephant'
>>> spam[-2]
'Rat'
>>> spam[7]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> spam[1:2]
['Bat']
>>> spam[0:2]
['Cat', 'Bat']
>>> spam = 'Hello'
>>> spam = [10, 20, 30]
>>> spam[1] = 40
>>> spam
[10, 40, 30]
>>> spam [1:3] = ['cat', 'dog', 'mouse']
>>> spam
[10, 'cat', 'dog', 'mouse']
>>> spam[:2]
[10, 'cat']
>>> spam[2:]
['dog', 'mouse']
>>> del spam[2]
>>> spam
[10, 'cat', 'mouse']
>>> del spam[1]
>>> spam
[10, 'mouse']
>>> del spam[1]
>>> spam
[10]
>>> len([1,2,3])
3
>>> [1,2,3] + [4,5]
[1, 2, 3, 4, 5]
>>> list(2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not iterable
>>> list('Hello')
['H', 'e', 'l', 'l', 'o']
>>> 'e' in list('Hello')
True
>>> 'f' in list('Hello')
False
>>> 'e' not in list('Hello')
False
>>> range(4)
range(0, 4)
>>> list(range(0,40))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]
>>> list(range(0,40, 5))
[0, 5, 10, 15, 20, 25, 30, 35]
>>> supplies = ['pens', 'staplers', 'binders', 'pencils']
>>> for i in range(len(supplies)):
...     print('index ' + str(i) + ' is ' + supplies[i)
  File "<stdin>", line 2
    print('index ' + str(i) + ' is ' + supplies[i)
                                                 ^
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>>     print('index ' + str(i) + ' is ' + supplies[i])
  File "<stdin>", line 1
    print('index ' + str(i) + ' is ' + supplies[i])
    ^
IndentationError: unexpected indent
>>> for i in range(len(supplies)):
...     print('index ' + str(i) + ' is ' + supplies[i])
... 
index 0 is pens
index 1 is staplers
index 2 is binders
index 3 is pencils
>>> 
>>> 
>>> cat = ['fat', 'orange', 'loud']
>>> size, colour, disposition = cat
>>> size
'fat'
>>> size, colour, disposition = 'skinny', 'black', 'quiet'
>>> a = 'AAA'
>>> b = 'BBB'
>>> a,b = b, a
>>> a
'BBB'
>>> b
'AAA'
>>> 