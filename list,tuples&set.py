### List, tuples and set

#list

courses = ['History','Maths','Physics','English']

print(courses) # ['history', 'Maths', 'Physics', 'English']
print(len(courses)) # 4
print(courses[3]) # English

# we can get the last item using index -1
print(courses[-1]) # English

# if we want to access the range of values

print(courses[0:2]) # ['history', 'Maths']

print(courses[:2]) # ['history', 'Maths']

print(courses[2:]) # ['Physics', 'English'] this is known as slicing

# add an item to the end of our list

courses.append('Art')

print(courses) # ['History', 'Maths', 'Physics', 'English', 'Art']

# add an item to a particular index of our list

# such as first index

courses.insert(1,'Art')

print(courses) # ['History', 'Art', 'Maths', 'Physics', 'English', 'Art']

# when we want to add multiple values using Extend

courses = ['History','Maths','Physics','English']
courses_2 = ['Art','Education']

courses.insert(0,courses_2)

print(courses) # [['Art', 'Education'], 'History', 'Maths', 'Physics', 'English']

print(courses[0])  # ['Art', 'Education'] the result is that both these values are included at index 0 instead of having separate index


courses = ['History','Maths','Physics','English']
courses_2 = ['Art','Education']
courses.extend(courses_2)

print(courses) # ['History', 'Maths', 'Physics', 'English', 'Art', 'Education']

# if we want to remove a value

courses.remove('Maths') # ['History', 'Physics', 'English', 'Art', 'Education']

# another method to remove values is using pop()
# by default it deletes the last value from the list

courses.pop() 
print(courses)  # ['History', 'Physics', 'English', 'Art']

# it also returns the value it deleted by following ways

popped = courses.pop() 

print(popped) # art
print(courses) # ['History', 'Physics', 'English']

# sorting the list


courses = ['History','Maths','Physics','English']

# if we want to reverse

courses.reverse()

print(courses) # ['English', 'Physics', 'Maths', 'History']

# if we want to sort in alphabetical order

courses.sort()
print(courses) # ['English', 'History', 'Maths', 'Physics']

# if we use numbers then it will order them ascendingly

nums = [1,4,6,3,9]

nums.sort() 
print(nums) # [1, 3, 4, 6, 9]

# if we want it to sort in descending order then

nums.sort(reverse = True) 
print(nums) # [9, 6, 4, 3, 1]

# now if we wanted a sorted list without altreing our original list
courses = ['History','Maths','Physics','English']
sorted(courses)
print(courses) # it didnot sort it ['History', 'Maths', 'Physics', 'English']
sorted_courses = sorted(courses)
print(sorted_courses) # ['English', 'History', 'Maths', 'Physics'] now the result is sorted

# built in functions mix, max and sum

print(min(nums)) # 1

print(max(nums)) # 9

print(sum(nums)) # 23

# if we want to serach for index for some value then
courses = ['History','Maths','Physics','English']

print(courses.index('English')) # 3

# if we want to check if a value is in the list or not then 

print('Art' in courses) # False
print('Maths' in courses) # True

for item in courses:
	print(item) 
#History
#Maths
#Physics
#English

# here item could be anything

# to get the index and value by using enumerate function

for index,course in enumerate (courses):
	print(index,course)

#(0, 'History')
#(1, 'Maths')
#(2, 'Physics')
#(3, 'English')

# if we want to add a start value to our index instead of 0 then

for index,course in enumerate (courses,start = 1):
	print(index,course)
#(1, 'History')
#(2, 'Maths')
#(3, 'Physics')
#(4, 'English')

# change list to a string

course_str = ', '. join(courses)

print(course_str) # History, Maths, Physics, English

# converst string to a list

new_list = course_str.split(', ')
print(new_list) # ['History', 'Maths', 'Physics', 'English']

### tuples

# tuples are immutable while list are mutables
# lets first see a mutable example:
list_1 = ['History','Maths','Physics','English']
list_2 = list_1

print(list_1) # ['History', 'Maths', 'Physics', 'English']
print(list_2) # ['History', 'Maths', 'Physics', 'English']

list_1[0] = 'Art'
print(list_1) # ['Art', 'Maths', 'Physics', 'English']
print(list_2) # ['Art', 'Maths', 'Physics', 'English']

# here we can see that our list list2 is also changed
# lets see example for immuatble:

tuples_1 = ('History','Maths','Physics','English')
tuples_2 = tuples_1

print(tuples_1) # ('History', 'Maths', 'Physics', 'English')
print(tuples_2) # ('History', 'Maths', 'Physics', 'English')

#tuples_1[0] = 'Art'
#print(tuples_1) # it throws an error because it cant mutates the list
#print(tuples_2) #

### sets

# are value which are unordered and no duplicates

cs_courses = {'History','Maths','Physics','English'}
print(cs_courses) # set(['Maths', 'English', 'Physics', 'History']) 

# here we can notice that it does not retain the same order we gave and also it changes everytime we run the print command

# now lets see how it removes duplicates

cs_courses = {'History','Maths','Physics','English','Maths'}
print(cs_courses) # set(['Maths', 'English', 'Physics', 'History'])

# sets are best when we need to check if a value is there in our sets or not
print('Maths' in cs_courses) # true

# it can also quickly tell what value it shares or not shares with other sets
cs_courses = {'History','Maths','Physics','English'}
art_courses = {'History','Maths','Art','Design'}

# to find what courses are common in both of these sets

print(cs_courses.intersection(art_courses)) # set(['Maths', 'History'])

# if i wanna see what are in cs_courses but are not in art_courses
print(cs_courses.difference(art_courses)) # set(['Physics', 'English'])

# If i wanna see all the courses offered by both of them 

print(cs_courses.union(art_courses)) # set(['Art', 'Design', 'English', 'Maths', 'Physics', 'History'])

# how to create empty list, tuples and sets

empty_list = []
empty_list = list()

empty_tuple = ()
empty_tuple = tuple()

empty_set = {} # this is not a set, this is an empty dictionary instead
empty_set = set()


