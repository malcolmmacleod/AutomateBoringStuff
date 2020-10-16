>>> spam = ['hello','hi','howdy','hiya']
>>> spam.index('hi')
1
>>> spam.index('h')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: 'h' is not in list
>>> spam.append('yo')
>>> spam
['hello', 'hi', 'howdy', 'hiya', 'yo']
>>> spam.insert(1, 'boo')
>>> spam
['hello', 'boo', 'hi', 'howdy', 'hiya', 'yo']
>>> # this is a comment
>>> spam.remove('boo')
>>> spam
['hello', 'hi', 'howdy', 'hiya', 'yo']
>>> # lists with numbner values and lists with string values can be sorted
>>> spam = [2, 5, 1 ,4, 7, 8, -1]
>>> spam.sort()
>>> spam
[-1, 1, 2, 4, 5, 7, 8]
>>> spam.sort(reverse= true)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'true' is not defined
>>> spam.sort(reverse=true)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'true' is not defined
>>> spam.sort(reverse=True)
>>> spam
[8, 7, 5, 4, 2, 1, -1]
>>> spam = ['Alice', 'Bob', 'andrew', 'bill']
>>> spam.sort()
>>> spam
['Alice', 'Bob', 'andrew', 'bill']
>>> spam = ['Alice', 'Bob', 'andrew', 'bill']
>>> spam.sort(key=str.lower)
>>> spam
['Alice', 'andrew', 'bill', 'Bob']
>>> 
