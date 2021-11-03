print('My age is ' + str(42))
print('Hello', 'world', sep=' ')
print('Hello', 'world', sep='\n')
print('home', 'user', 'documents', sep='/')
print(' '.join(['jdoe is', str(42), 'years old']))
print(str(1), 'Python Tricks', 'Dan Bader', sep=',')
#This prints out "John is 23 years old"
name ='John'
#Proffesional way: % is a place hold for name(as set by "% name")
#%s converts whatever % is into a string (the s) can also be converted to other data types 
print('Hello, %s!' % name)
print('There\'s a snake in my boot!')
c = 'cats' [0]
n = 'Ryan' [3]
print(c)
print(n)
print('Ryan'.lower())
print('Ryan'.upper())
name = 'sameerah'
print(len(name))
x = input('Enter value of X:')
y = input('Enter value of y:')
print(x)
print(y)
temp = x
x = y
y = temp
print('The value of x after swapping: {}' .format(x))
print('The value of y after swapping: {}' .format(y))
