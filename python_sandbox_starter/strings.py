# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Brad'
age = 37

# Concatenate only Str
# print('Hello, my name is ' + name + ' and I am ' + str(age))


# String Formatting


# Arguments by position
# print('My name is {name} and I am {age}'.format(name=name, age=age))

# F-Strings (3.6+)
# print(f'Hello, my name is {name} and I am {age}')


# String Methods
s = 'hello world'

# Cap str
print(s.capitalize())

s.upper()
s.swapcase()
len(s)
s.replace('world', 'everyone')

# Count 
sub = 'h'
print(s.count(sub)) # count how many 'h's in string s

s.startwith('hello')  # true

# Split into a list/arr
s.split()

# Find position
s.find('r')

# Is all alphanumeric
s.isalnum()

s.isalpha()
s.isnumeric()

