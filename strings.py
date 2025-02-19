# Strings in Python

str="hello"
print(str)

print(str[0])
print(str[1])
# reverse indexing print from last
print(str[-1])

# slicing
print(str[1:4])
# print from start to 4
print(str[:4])
# print from 1 to end
print(str[1:])
# gap of 2
print(str[1:5:2])

# string concatenation
str1="hello"
str2="world"
print(str1+str2)

# length of string
print(len(str1))

# string repetition
print(str1*3)

# string membership

str2="hello"

print('h' in str2)

# function in string

str3="hello world"

# ascending order ma sort garxa string
print(sorted(str3))

# descending order ma sort garxa string
print(sorted(str3,reverse=True))


# string methods
print(str3.upper())
print(str3.lower())
print(str3.capitalize())
print(str3.title())
print(str3.swapcase())
print(str3.find('world')) # find the index of the word
print(str3.replace('world','python')) # replace the word
print(str3.split(' ')) # split the string
#  list bata string ma convert garxa
print(' '.join(['hello','world']))
print(str3.count('l')) # count the number of character
# strip remove the white space
print(str3.strip())

