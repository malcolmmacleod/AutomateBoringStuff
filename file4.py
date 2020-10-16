>>> os.unlink('hello.txt')
>>> os.rmdir('test3')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
OSError: [Errno 66] Directory not empty: 'test3'
>>> os.chdir('test3')
>>> os.unlink('hello.txt')
>>> os.chdor('..')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'os' has no attribute 'chdor'
>>> os.chdir('..')
>>> os.rmdir('test3')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
OSError: [Errno 66] Directory not empty: 'test3'
>>> 
>>> 
>>> import shutil
>>> shutil.rmtree('test3')

