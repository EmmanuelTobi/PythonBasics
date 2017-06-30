#some string operations to enjoy

#formating
'{0}, {1}, {2}'.format('a', 'b', 'c')
'Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W')
#output: 'Coordinates: 37.24N, -115.81W'

#comma as a thousands separator
'{:,}'.format(1234567890)
#output: '1,234,567,890'

#dictionaries
values = (3, 5)
'X: {0[0]};  Y: {0[1]}'.format(values)
#output: 'X: 3;  Y: 5'

#string indexing and slicing
print ("Python rocks!") #to print the string including the space

len("Python rocks!") #to get total length of the string above
#output: 13

#positive indexing for "Python rocks!"; 0 1 2 3 4 5 6 7 8 9 10 11 12

#negative indexing for "Python rocks!"; -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1

#automatically in python strings are provided with the attributes of some few list methods without the actual use of list()
#except append, pop, insert and others but the main methods are len(), .find(char), .count(char) and slicing

#slicing
#you can change the numbers to get more outputs
a = "Python rocks!"
print(a[:6])
#Output: 'Python'

print(a[5])
#output: 'n'

print(a[7:])
#Output: 'rocks'

print(a[7:11])
#output: 'rocks'

print(a[::-1])
#output: skcor nohtyP

print(a[::-2])
#output: '!ko otP'

print(a[-4:-1])
#output: 'ock!'

#counting number a characters in a string
a.count("o")
#output: 2

#finding position of a character in a string
b = "fish"
b.find(h)
#output: 3