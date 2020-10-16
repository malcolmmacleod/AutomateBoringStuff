def hello():
    print('Howdy')
    print('Howdy!!!')

hello()
hello()
hello()

# parameter
def helloName(name):
    print ('Hello ' + name)

helloName('Alice')
helloName('Bob')

#return

def plusOne(number):
    return number + 1

answer = plusOne(7)
print(answer)


# keyword arguments
print('Hello', end='')
print('cat', 'dog', sep=' ')

