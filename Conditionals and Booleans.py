if True:
	print('condition was true') # condition was true


if False:
	print('condition was true') #Nothing happens .. it says PATH: command not found


#Comparisions:
#Equal: 				==
#Not Equal 				!=
#Greater Than			>
#Less Than				<
#Greater or Equal		>=
#Less or Equal			<=
#Object Identity		is

#Boolean operations:
#and
#or
#not

# to determine what python evaluates to be true or false: its easier to find what are false evaluation and then we know rest are true
# False Values:
	#False
	#None
	#Zero of any numeric type
	#Any empty sequence.For example, '',(),[]
	#Any empty mapping. For example, {}

condition = False

if condition:
	print('Evaluated to True')
else:
	print('Evaluated to False') # Evaluated to False

condition = None

if condition:
	print('Evaluated to True')
else:
	print('Evaluated to False') # Evaluated to False

# zero will evaluted to false

condition = 0

if condition:
	print('Evaluated to True')
else:
	print('Evaluated to False') # Evaluated to False

condition = 5

if condition:
	print('Evaluated to True')
else:
	print('Evaluated to False') # Evaluated to True

condition = []

if condition:
	print('Evaluated to True')
else:
	print('Evaluated to False') # Evaluated to False

condition = {}

if condition:
	print('Evaluated to True')
else:
	print('Evaluated to False') # Evaluated to False

# rest all the conditions other than above will evaluate to be true. For Ex:

condition = 'Test'

if condition:
	print('Evaluated to True')
else:
	print('Evaluated to False') # Evaluated to True

#Comparisions:

language = 'Python'

if language == 'Python':
	print('Language is Python')  #condition was true Language is Python
else:
	print('No Match') # Language is Python

language = 'Java'

if language == 'Python':
	print('Language is Python')  #condition was not true 
else:
	print('No Match') # No Match


if language == 'Python':
	print('Language is Python')  #condition was not true 
elif language == 'Java':
	print('Language is Java')  #condition was true - Language is Java
else:
	print('No Match') #condition was not true 


#is when two objects are equal but not same in the memory

a = [1,2,3]
b = [1,2,3]

print(a == b) # True

print( a is b) # False

# to print the location of these two objects use id() function

print(id(a)) # 4317924888
print(id(b)) # 4317925320
print( a is b) # False

# if we would have define them differently then:

a = [1,2,3]
b = a
print(id(a)) # 4517043376
print(id(b)) # 4517043376
print( a is b) # True

# now both of them have same id's because now they are same objects in the memory

print(id(a) == id(b)) # True



#Boolean
#and

user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
	print('Admin Page')  # Admin Page
else:
	print('Bed Creds')


user = 'Admin'
logged_in = False

if user == 'Admin' and logged_in:
	print('Admin Page')  # condition not true
else:
	print('Bed Creds') # Bed Creds

# or

user = 'Admin'
logged_in = False

if user == 'Admin' or logged_in:
	print('Admin Page')  # Admin Page
else:
	print('Bed Creds')

#not

user = 'Admin'
logged_in = True

if not logged_in:    
	print('Please Log in')
else:
	print('Welcome') # Welcome


user = 'Admin'
logged_in = False

if not logged_in:    
	print('Please Log in') # Please Log in
else:
	print('Welcome') 






