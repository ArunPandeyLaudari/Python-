#explain defination of builtin module and how to use it
# Builtin modules are modules that are already present in the python library.
# These modules are written in C and integrated with the python interpreter.

# Python has a lot of built-in modules that help us in many ways. Some of the built-in modules are:

# math
# random
# os
# sys
# datetime
# time
# json
# re
# calendar
# collections
# operator
# functools
# itertools
# sqlite3
# tkinter
# requests
# etc.

# help('modules') # to see all the modules available in python

# if we want to use any of the built-in modules, we need to import them first.

# import math
# import random
# import os
# import sys
# import datetime
# import time



#eg using math module

import math
print(math.sqrt(5))
print(math.pow(2,3))
print(math.pi)
print(math.e)
print(math.floor(2.9))
print(math.ceil(2.1))
print(math.factorial(5))

#eg using random module
import random

print(random.random()) # random number between 0 and 1
print(random.randint(1,10)) # random number between 1 and 10
# print(random.choice([1,2,3,4,5,6,7,8,9])) # random number from the list
# print(random.choice('hello')) # random character from the string
print(random.shuffle([1,2,3,4,5,6,7,8,9])) # shuffle the list

#eg using os module


import os
print(os.getcwd()) # get current working directory
print(os.listdir()) # list of files and directories in the current directory
print(os.path.exists('areaofcircle.py')) # check if the file exists or not
print(os.path.isfile('areaofcircle.py')) # check if the given path is file or not
print(os.path.isdir('areaofcircle.py')) # check if the given path is directory or not
print(os.path.join('C:/Users/HP/Desktop/python','test.txt')) # join the path


#eg using sys module 
import sys
print(sys.argv) # get the command line arguments
print(sys.version) # get the python version
print(sys.path) # get the python path
print(sys.platform) # get the platform

#eg using datetime module
import datetime
print(datetime.datetime.now()) # get the current date and time
print(datetime.date.today()) # get the current date
print(datetime.datetime.now().year) # get the current year
print(datetime.datetime.now().month) # get the current month
print(datetime.datetime.now().day) # get the current day
print(datetime.datetime.now().hour) # get the current hour
print(datetime.datetime.now().minute) # get the current minute
print(datetime.datetime.now().second) # get the current second
print(datetime.datetime.now().microsecond) # get the current microsecond


#eg using time module
import time
print(time.time()) # get the current time in seconds
print(time.localtime()) # get the current time in local time

