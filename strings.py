 'Hello'
'Hello'
>>> "That is Alice's cat"
"That is Alice's cat"
>>> 'Say hi to Bob\'s mother'
"Say hi to Bob's mother"
>>> "\"hi\", I said"
'"hi", I said'
>>> print ("hello there \nho are you"
... 
... )
hello there 
ho are you
>>> r'Hello'
'Hello'
>>> r'That is Catol\'s cat'
"That is Catol\\'s cat"
>>> # r is raw string
>>> ''' this 
... is 
... a multiline
... string'''
' this \nis \na multiline\nstring'
>>> print('''this
... is
... multiline 
... string''')
this
is
multiline 
string
>>> print("""This 
... also 
... is  a
... multiline
... string""")
This 
also 
is  a
multiline
string
>>> spam = 'Hello world'
>>> spam[0]
'H'
>>> spam[3:5)
  File "<stdin>", line 1
    spam[3:5)
            ^
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>> spam[3:5]
'lo'
>>> 'Hello' in spam
True
>>> 'HELLO' in spam
False
>>> 