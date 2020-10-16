>>> # string methods return a new string as strings are immutable
>>> spam = 'Hello world'
>>> spam2 = spam.upper()
>>> spam
'Hello world'
>>> spam2
'HELLO WORLD'
>>> spam3 = spam2.lower()
>>> spam3
'hello world'
>>> spam2
'HELLO WORLD'
>>> spam2.isUpper()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'isUpper'
>>> spam2.isupper()
True
>>> spam3.isupper()
False
>>> spam3.islower()
True
>>> 'Hello'.upper()
'HELLO'
>>> 'Hello'.upper().isUpper()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'isUpper'
>>> 'Hello'.upper().isupper()
True
>>> '1234'.isalnum()
True
>>> '1234'.isdecimal()
True
>>> '1234'.isalpha()
False
>>> 'Malcolm'.istitle()
True
>>> 'hello'.istitle()
False
>>> '   '.isspace() 
True
>>> 'hello world'.title()
'Hello World'
>>> 'Hello'.startswith('He')
True
>>> 'Hello'.endswith('lo')
True
>>> ','.join(['Cats', 'Rats', 'Bats'])
'Cats,Rats,Bats'
>>> ' '.join(['Cats', 'Rats', 'Bats'])
'Cats Rats Bats'
>>> 'Cats Rats Bats'.split()
['Cats', 'Rats', 'Bats']
>>> 'Cats,Rats,Bats'.split(',')
['Cats', 'Rats', 'Bats']
>>> 'Hello'.rjust(10)
'     Hello'
>>> 'there'.ljust(10)
'there     '
>>> 'hello'.center(20)
'       hello        '
>>> '     Hello    '.strip()
'Hello'
>>> '    Hello    '.lstrip()
'Hello    '
>>> '    Hello    '.rstrip()
'    Hello'
>>> 'SpamSpamBaconSpamSpam).strip('Bacon')
  File "<stdin>", line 1
    'SpamSpamBaconSpamSpam).strip('Bacon')
                                   ^
SyntaxError: invalid syntax
>>> 'SpamSpamBaconSpamSpam').strip('Bacon')
  File "<stdin>", line 1
    'SpamSpamBaconSpamSpam').strip('Bacon')
                           ^
SyntaxError: unmatched ')'
>>> 'SpamSpamBaconSpamSpam'.strip('Bacon')
'SpamSpamBaconSpamSpam'
>>> 'SpamSpamBaconSpamSpam'.strip('B')
'SpamSpamBaconSpamSpam'
>>> 'SpamSpamBaconSpamSpam'.strip('Spam')
'Bacon'
>>> 'SpamSpamBaconSpamSpam'.replace('Bacon', '')
'SpamSpamSpamSpam'
>>> 