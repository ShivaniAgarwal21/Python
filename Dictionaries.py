# dictionaries works with key-value pairs

student = {'name': 'John', 'age': 25,'Courses': ['Maths','English']}
print(student) # {'Courses': ['Maths', 'English'], 'age': 25, 'name': 'John'}
print(student['name']) # John
# key could be integer or string and other data types too
# in order to get sensible outputs other than throwing error for the key results use get method 
print(student.get('name')) # John
print(student.get('phone')) # None
# too set up default messgae for keys not found:
print(student.get('phone','Not Found')) # Not Found

# how to add a new key to our dictionary
student ['phone'] = '555-555-5555'
print(student) # {'Courses': ['Maths', 'English'], 'age': 25, 'name': 'John', 'phone': '555-555-5555'}
# if we do the step at line 14 for a key which already exist then it will simply update the value of existing one:
student['name'] = 'Jane'
print(student) # {'Courses': ['Maths', 'English'], 'age': 25, 'name': 'Jane', 'phone': '555-555-5555'}
# if we want to update multiple values in dictionary then:
student.update({'name': 'Shivani', 'phone': '444-444-4444', 'fathers name': 'Anil'})
print(student) # {'Courses': ['Maths', 'English'], 'name': 'Shivani', 'phone': '444-444-4444', 'age': 25, 'fathers name': 'Anil'}
# if u want to delete a key then
del student['fathers name']
print(student) # {'Courses': ['Maths', 'English'], 'name': 'Shivani', 'phone': '444-444-4444', 'age': 25}
## another method of deleting key and value is using pop method as in list
age_1 = student.pop('age')
print(student,age_1) # ({'Courses': ['Maths', 'English'], 'name': 'Shivani', 'phone': '444-444-4444'}, 25)
# check the length of dictionary
print(len(student))  # 3
# if we want to see keys in it:
print(student.keys()) # ['Courses', 'name', 'phone']
# for values
print(student.values()) # [['Maths', 'English'], 'Shivani', '444-444-4444']
# if we want to see keys and values then
print(student.items()) #   [('Courses', ['Maths', 'English']), ('name', 'Shivani'), ('phone', '444-444-4444')]
# to loop through all the keys and values:
for key in student:
	print(key)
#Courses
#name
#phone

# this way only keys were printed to print value as well follow next step:
for key,value in student.items():
	print(key,value)
#('Courses', ['Maths', 'English'])
#('name', 'Shivani')
#('phone', '444-444-4444')