>>> cat = {'name': 'Zophie', 'age': 7, 'colour': 'grey'}
>>> allCats = []
>>> allCats.append(cat)
>>> allCats
[{'name': 'Zophie', 'age': 7, 'colour': 'grey'}]
>>> allCats.append({'name': 'Zophie', 'age': 3, 'colour': 'black'}
... 
... )
>>> allCats
[{'name': 'Zophie', 'age': 7, 'colour': 'grey'}, {'name': 'Zophie', 'age': 3, 'colour': 'black'}]
>>> 
>>> 
>>> 
>>> theBoard = {'top-L': '', 'top-M: '', 'top-R': '',
  File "<stdin>", line 1
    theBoard = {'top-L': '', 'top-M: '', 'top-R': '',
                                          ^
SyntaxError: invalid syntax
>>> # can use a dictionary to represent a knots and crosses board
>>> theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'middle-L': ' ', 'middle-M': ' ', 'middle-R': ' ', 'bottom-L': ' ', 'bottom-M': ' ', 'bottom-R': ' '}
>>> import pprint
>>> pprint.pprint(theBoard)
{'bottom-L': ' ',
 'bottom-M': ' ',
 'bottom-R': ' ',
 'middle-L': ' ',
 'middle-M': ' ',
 'middle-R': ' ',
 'top-L': ' ',
 'top-M': ' ',
 'top-R': ' '}
>>> theBoard['middle-M'] = 'X'
>>> theBoard
{'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'middle-L': ' ', 'middle-M': 'X', 'middle-R': ' ', 'bottom-L': ' ', 'bottom-M': ' ', 'bottom-R': ' '}
>>> pprint.pprint(theBoard)
{'bottom-L': ' ',
 'bottom-M': ' ',
 'bottom-R': ' ',
 'middle-L': ' ',
 'middle-M': 'X',
 'middle-R': ' ',
 'top-L': ' ',
 'top-M': ' ',
 'top-R': ' '}
>>> def printBoard(board):
...     print(board['top-L' + '|' + board['top-M' + '|' + board['top-R'])
  File "<stdin>", line 2
    print(board['top-L' + '|' + board['top-M' + '|' + board['top-R'])
                                                                    ^
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>>     print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
  File "<stdin>", line 1
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    ^
IndentationError: unexpected indent
>>> def printBoard(board):
...     print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
... 
>>> printBoard(theBoard)
 | | 
>>> def printBoard(board):
...     print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
...     print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
...     print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
... 
>>> 
>>> 
>>> type(42)
<class 'int'>
>>> type 'hello')
  File "<stdin>", line 1
    type 'hello')
         ^
SyntaxError: invalid syntax
>>> type ('hello')
<class 'str'>
>>> type(theBoard)
<class 'dict'>
>>> 
