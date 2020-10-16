>>> import os
>>> os.path.join('folder1', 'folder2', 'folder3', 'file.txt')
'folder1/folder2/folder3/file.txt'
>>> os.sep
'/'
>>> os.getcwd()
'/Users/malcolmmacleod/Documents/Developer/python/AutomateBoringStuff'
>>> os.chdir('/Users/malcolmmacleod/Documents/Developer/')
>>> os.getcwd()
'/Users/malcolmmacleod/Documents/Developer'
>>> .
  File "<stdin>", line 1
    .
    ^
SyntaxError: invalid syntax
>>> os.chdir(..)
  File "<stdin>", line 1
    os.chdir(..)
             ^
SyntaxError: invalid syntax
>>> os.chdir('..')
>>> os.getcwd()
'/Users/malcolmmacleod/Documents'
>>> os.chdir('./Developer')
>>> os.getcwd()
'/Users/malcolmmacleod/Documents/Developer'
>>> os.path.abspath('./Developer')
'/Users/malcolmmacleod/Documents/Developer/Developer'
>>> os.path.isabs('/Users/malcolmmacleod/Documents/Developer/Developer')
True
>>> os.path.isabs('/Developer/Developer')
True
>>> os.path.isabs('/Developer')
True
>>> os.path.relpath('/Developer')
'../../../../Developer'
>>> pwd
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'pwd' is not defined
>>> os.path.dirname('list3.py')
''
>>> os.chdir('/Users/malcolmmacleod/Documents/Developer/python/AutomateBoringStuff')
>>> os.path.relpath('hello.py')
'hello.py'
>>> os.path.dirname('hello.py')
''
>>> os.chdir('/Users/malcolmmacleod/Documents/Developer/python/AutomateBoringStuff')
>>> os.path.dirname('/Users/malcolmmacleod/Documents/Developer/python/AutomateBoringStuff/true.py')
'/Users/malcolmmacleod/Documents/Developer/python/AutomateBoringStuff'
>>> os.path.basename('/Users/malcolmmacleod/Documents/Developer/python/AutomateBoringStuff/true.py')
'true.py'
>>> os.path.exists('/Users/malcolmmacleod/Documents/Developer/python/AutomateBoringStuff')
True
>>> os.path.isfile(('/Users/malcolmmacleod/Documents/Developer/python/AutomateBoringStuff')
... 
... 
KeyboardInterrupt
>>> os.path.isfile('/Users/malcolmmmacleod/Documents/Developer/python/AutomateBoringStuff')
False
>>> os.path.isfile('/Users/malcolmmmacleod/Documents/Developer/python/AutomateBoringStuff/true.py')
False
>>> os.listdir(('/Users/malcolmmacleod/Documents/Developer/python/AutomateBoringStuff'))
['hello.py', 'list.py', 'error.py', 'charactercount.py', 'hundred.py', 'true.py', 'list3.py', 'game.py', 'hello-function.py', 'list2.py', 'formatting.py', 'while.py', 'whilenot.py', 'strings2.py', 'elif.py', 'for.py', 'password.py', '.vscode', 'script.py', 'dicts.py', 'scope.py', 'strings.py', 'moredicts.py']
>>> os.makedirs('test')
>>> os.listdir(('/Users/malcolmmacleod/Documents/Developer/python/AutomateBoringStuff'))
['hello.py', 'list.py', 'error.py', 'charactercount.py', 'test', 'hundred.py', 'true.py', 'list3.py', 'game.py', 'hello-function.py', 'list2.py', 'formatting.py', 'while.py', 'whilenot.py', 'strings2.py', 'elif.py', 'for.py', 'password.py', '.vscode', 'script.py', 'dicts.py', 'scope.py', 'strings.py', 'moredicts.py']
>>> 

