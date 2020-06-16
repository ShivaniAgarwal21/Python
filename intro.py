message = 'Hello world'
hello = 'Shivani\'s Hello'
multiple = """I like learning python
 python is very interesting 
 but the tools aren't that good"""
print(len(message),hello[2],multiple[0:6],multiple[:6]) # 11,'i','I like','I like'
# length of the string is given by len
# when we want to access a substring then use square bracket but remember that the first string will have index as 0
# when we use colon 0:6 then 0 value is included but 6th value is not
# When we do this [:6] that time also we will get the same results as it assumes to take it from first string
# to print hello world all in small case then:
print(message.lower()) # hello world

# to print hello world all in upper case then:
print(message.upper()) # HELLO WORLD

# if we want to count how many times a string appears in our message then:
print(message.count('Hello')) # 1
print(message.count('l')) # 3

# if we want to find a string appears at what position in our message then:

print(message.find('world')) # 6
print(message.find('World')) # -1 because it cant find this string with capital W anywhere

# if we want to replace a string appears in our message with some other string then:

nw_message = message.replace('world','Universe') # here we are replacing world with Universe in message

print(nw_message) # Hello Universe

# if we want to add multiple strings and concatenate them together:

greeting = 'Hello'
name = 'Shivani'

message = greeting + name 

print(message) # HelloShivani

# if we want space between these two words then:

message = greeting + ', ' + name 

print(message) # Hello, Shivani

# using format string we can write the sentence as we want and wont have to take care of the + signs and will be using placeholders instead

message = '{}, {}'. format(greeting,name) 
print(message) # Hello, Shivani

message = '{}, {}. Welcome!'. format(greeting,name) 
print(message) # Hello, Shivani

# f string method is introduced newly in 3.6 version python. Lets try that

# message = f '{greeting}, {name}' 
#print(message) # Hello, Shivani

# using dir we can see all of the methods or attributes that variable has access to

print(dir(message))

# now if we wanna see how to use these functions then use help on class string

print(help(str))

# if we want to know about any particular function or method then:

print(help(str.lower))

###Integers and Float

#Integer is whole number and float is decimal
num = 3
print(type(num)) # int

num = 3.4
print(type(num)) # float

print(3 + 2) # 5
print(3 - 2) # 1
print(3 * 2) # 6
print(3 / 2) # 1.5
print(3 // 2) # 1 known as floor division

# exponents
print(3 ** 2) # 3 to the power 2 = 9

# modulus

print(3 % 2) # 1 it tell us if the number is odd or even. If 0 then even if 1 then odd

print(3 * 2 + 1) # 7

print(3 * (2 + 1)) # 9

# how to increment a value by 1
num = 1

num = num +1

print(num) # 2

# another way to write it

num = 1

num += 1

print(num) # 2

# can use * also in place of + .. actually any airthmetic function

# absolute value

print(abs(-3))  # 3

# round will round the value to nearest integer value

print(round(3.75)) # 4

print(round(3.75,1)) # 3.8

# compairisions

# Equal :  		3 == 2
# Not Equal :  	3 != 2
# Greater than  3 > 2
# Less than 	3 < 2
# less or equal 3 <= 2

num_1 = 3
num_2 = 2

print( num_1 == num_2) # False
print( num_1 != num_2) # True
print( num_1 > num_2) # True
print( num_1 < num_2) # False
print( num_1 <= num_2) # False



# strings which looks like numbers

num_1 = '100'
num_2 = '200'

print(num_1 + num_2) # 100200 because this is string its concatenated

# to change it to integers
# we will use casting

num_1 = int(num_1)
num_2 = int(num_2)

print(num_1 + num_2) #300
