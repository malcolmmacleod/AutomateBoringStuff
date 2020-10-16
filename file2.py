>>> import os
>>> os.getcwd()
'/Users/malcolmmacleod/Documents/Developer/python/AutomateBoringStuff'
>>> open('hello.txt')
<_io.TextIOWrapper name='hello.txt' mode='r' encoding='UTF-8'>
>>> hello_file = open('hello.txt')
>>> hello_file = open('hello.txt')
>>> hello_file.read()
'this is a file\n'
>>> hello_file.CLOSE()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: '_io.TextIOWrapper' object has no attribute 'CLOSE'
>>> hello_file.close()
>>> hello_file = open('hello.txt')
>>> hello_file.readlines()
['this is a file\n']
>>> hello_file.close()
>>> 
>>> #write mode
>>> hello_file = open('hello.txt', 'w')
>>> hello_file.close()
>>> hello_file = open('hello2.txt', 'w')
>>> hello_file.write('Hello')
5
>>> he
hello_file help(      hex(      
>>> hello_file.close()
>>> hello_file = open('hello2.txt', 'w')
>>> hello_file.close()
>>> hello_file = open('hello2.txt', 'a')
>>> hello_file.write('this is a file\n is it good')
26
>>> hello_file.close()
>>> hello_file = open('hello2.txt', 'a')
>>> hello_file.write('this is some more text')
22
>>> hello_file.close()
>>> 
>>> 
>>> 
>>> 
>>> 
>>> import shelve
>>> shelf_file = shelve.open('mydata')
>>> shelf_file['cats'= = ['oreo', 'oscar', 'cleo']
  File "<stdin>", line 1
    shelf_file['cats'= = ['oreo', 'oscar', 'cleo']
                     ^
SyntaxError: invalid syntax
>>> shelf_file['cats'] = ['oreo', 'oscar', 'cleo']
>>> shelf_file.close()
>>> os.getcwd()
'/Users/malcolmmacleod/Documents/Developer/python/AutomateBoringStuff'
>>> os.listdir()
['hello.py', 'list.py', 'error.py', 'charactercount.py', 'test', 'hundred.py', 'true.py', 'list3.py', 'game.py', 'hello-function.py', 'list2.py', 'formatting.py', 'while.py', 'whilenot.py', 'mydata.db', 'strings2.py', 'file1.py', 'elif.py', 'for.py', 'hello2.txt', 'password.py', '.vscode', 'script.py', 'hello.txt', 'dicts.py', 'scope.py', 'strings.py', 'moredicts.py']
>>> 
