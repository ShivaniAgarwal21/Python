# For Loop
nums = [1,2,3,4,5]

for num in nums:
	print(num)

#1
#2
#3
#4
#5

# Break and Continue keywords:

for num in nums:
	if num == 3:
		print('We found it')
		break
	print(num) 
#1
#2
#We found it

for num in nums:
	if num == 3:
		print('We found it')
		continue
	print(num) 
#1
#2
#We found it
#4
#5

# Loop within the loop

for num in nums:
	for letter in 'abc':
		print(num,letter)
#(1, 'a')
#(1, 'b')
#(1, 'c')
#(2, 'a')
#(2, 'b')
#(2, 'c')
#(3, 'a')
#(3, 'b')
#(3, 'c')
#(4, 'a')
#(4, 'b')
#(4, 'c')
#(5, 'a')
#(5, 'b')
#(5, 'c')

# when we want to loop through certain times then use range()

for i in range(10):
	print(i)
#0
#1
#2
#3
#4
#5
#6
#7
#8
#9

# Now if do not wish to start with o then we can give a staring value: We gave range till 11 because it skips the last one

for i in range(1, 11):
	print(i)
#1
#2
#3
#4
#5
#6
#7
#8
#9
#10

# While Loop will go on until a certain condition is met or until we hit a break

x = 0

while x < 10:
	print(x)
	x += 1
#0
#1
#2
#3
#4
#5
#6
#7
#8
#9

# break
x = 0

while x < 10:
	if x == 5:
		break
	print(x)
	x += 1
#0
#1
#2
#3
#4

# to create an infinite loop or until we found some value:

x = 0

while True:
	if x == 5:
		break
	print(x)
	x += 1
#0
#1
#2
#3
#4

# if we ever stuck in infinite loop and want to exit that then use control + C
x = 0

while True:
#	if x == 5:
#		break
	print(x)
	x += 1

480702
480703
480704
[Cancelled]



