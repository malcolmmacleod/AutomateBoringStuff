>>> os.mkdir('./test2')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'os' is not defined
>>> os.mkdir('test2')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'os' is not defined
>>> import os
>>> os.mkdir('test2')

>>> shutil.copytree('./test', './test3')
'./test3'
>>> shutil.move('./test2', './test3')
'./test3/test2'
>>> # use move rather than rename