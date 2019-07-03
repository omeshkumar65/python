#!/usr/bin/env python
# coding: utf-8

# In[18]:


# this is a comment
#There is no multiline comment in python
'''thi syntax is used to show string and used as a comment in class and functions'''


# In[29]:


# this is the datatype learning
a=5       # variable datatype is know by it,s value
b="is"
c='this is a string'
print(a)
print(b)
print(c)
a = b = c = 7.777777777777777
print(a)
print(b)
print(c)


# In[45]:


# range function
var = 'hello world'
var2 = "omesh kumar"
print(var[0:4])
print(var2[:10])
print(var2[-6:-1])


# In[67]:


#List in python
list = ['hello', 4,5,"world",66]
print(list * 8)
print(list[3])
print(list[0:3])


# In[82]:


# Tuples
# Tuples is same  as the list
# but difference is:- in lis we assign the value at any location but we canot do in tuples
list = ['hello',5,6,"world"]
print(list[0])
print(list[1])
list[0]=5
list[1]='hello'
print(list[0])
print(list[1])

# In Tuples
tuples=('hello',5,6,"world")
print(tuples)
print(tuples[0])
print(tuples[1])
tuples[0]='hello'     # In tuples we cann't assign value. So, it gives error


# In[87]:


# Some test of list and tuples
list['hello',5,4,'world']
print(list)
list[0:4] = range(0,4)    # range(). range is a predefined function


# In[106]:


# Dictionary
dictionary = {1: 'hello', 2: 5,"hello":6}
print(dictionary)
print(dictionary[1])
print(dictionary['hello'])
dictionary['hello'] = 'hello welcome'
print(dictionary)
print(dictionary.values())
print(dictionary.keys())

# This given below line gives error:- multiplication(*) and addition(+) operator didn't work
#print(dictionary + dictionar)
#print(dictionary * 2)
# same with these two given lines
#print(dictionary.values())
#print(dictionary.keys())


# In[52]:


# Data type conversion
for i in range(65,91):
    print(i,"=",chr(i),' ',end='')
print("\n",end='')
for i in range(97,122):
    print(chr(i))
    


# In[62]:


# Bitwise Operator

var1 = 10           # 1010
var2 = 3            # 0011
#                    -------
# AND                 0010 (2)
print(var1 & var2)
# OR                  1011 (11)
print(var1 | var2)
# EXOR                1001 (9)
print(var1 ^ var2)

var3 = 10          # 1010 
#                    ------
# NOT                0101 (0)

print(~var3)

#LEFT SHIFT:- 

print(var3 <<1)


# In[6]:


# Logical Operator

var1 = True
var2 = True
var3 = False
var4 = False

# And operator

print(var1 and var2 )
print(var1 and var3 )

# OR operator
print(var1 or var2)
print(var1 or var3 )

# NOT operator

print(not(var1))
print(not(var3))


# In[10]:


# Membership operator
String = "Omesh Kumar"

print('o' in String)   # small letter 'o'
print('O' in String)   # capital letter 'O' 
print('m' not in String)
print('z' not in String)


# In[15]:


# Identity operator

var1 = 10
var2 = 10
var3 = 15

# var1 = 'omesh'
# var2 = 'omesh'
# var3 = 'kapil'

print(var1 is var2)
print(var1 is not var2)
print(var1 is var3)


# In[17]:


# Operator precedence

var1 = 5 ** 2 + 7
var2 = 5 + 7 ** 2
print(var1)
print(var2)


# In[92]:


# Loops
var = 'Hellozworld'
var1 = 'Welcome'
for i in var:
    print(i,end='')
while len(var)>len(var1):
    print('\nH')
    break
for i in var:
    if i == 'z':
        pass
        print('there is a space')
    print(i)


# In[63]:


# Math library

import math
print(math.exp(2))   # math.exp(2) = e^2
var = math.exp(1)    # math.exp(1) = e^1
print(var ** 2)
var2 = 5
print(math.sqrt(25))

var3 = math.sin(math.pi)
print("sin(180)=",var3)
print("sin(180)=",float(var3))
print("sin(180)=",int(var3))

var4 = math.cos(math.pi/2)
print("cos(90)=",var4)
print("cos(90)=",float(var4))
print("cos(90)=",int(var4))

print(math.e)


# In[89]:


# String
string = "Hello world"
print(string[1:5])
print(string[:5])
print(string[1:])
string1 = "wel"
string2 = "come"

print("%s is the welcome message %s", (string1,string2))
print("%s is the welcome message %s" % (string1,string2))
print(string + " " + string1 + string2 + " this way")

var3 = "hello world"
print(var3.capitalize())
for i in var3:
    print(i.capitalize(),end='')


# In[12]:


# del and len()

# List
list1 = [1,2,34,'hello',45,'omesh kumar']
print(list1)
print('length of list = ',len(list1))
del list1[1]
print(list1)
print('length of list = ',len(list1))

# tuples
tuples1=(1,2,3,'hello',"omesh kumar")
print("tuples1=",tuples1)
print("length of tuples1=",len(tuples1))
# tuples1[7]=6                           #tuples don't support assignment of values  
del tuples1
print("after delete")
#print("tuples1=",tuples1)                #This gives error because tuples1 is deleted
#print("length of tuples1=",len(tuples1))


# In[2]:


# Time

import time
import calendar

print(time.time())
local = time.localtime(time.time())
print(local)
formated = time.asctime(time.localtime(time.time()))
print(formated)
print("calendar")
print(calendar.month(2019,6,4,2))  # 2019 is year, 6 is month,4 is number of spacesbetween columns,2 is number of spaces in rows

# find from google
from datetime import date
today1 = date.today()
print(today1)


# In[18]:


# functions
def awesomefunction():
    print("this is a function")
    return
awesomefunction()

def PassArguments(number1, number2):
    print("there are two arguments")
    return number1+number2

print(PassArguments(5,6))


# In[61]:


# Modules
import math
print(math.pi)

from math import pi
print(pi)

# dir function
contents = dir(math)
print(contents)

print(math.log(math.exp(1)))
print(math.pow(2,3))
print(math.sin(math.pi/2))

#the value give by give below code i almost zero, see how i happen
print(math.cos(math.pi/2))

a=math.cos(math.pi/2)
print(a)
print(int(a))

import time
b = dir(time)
print(b)

print("\n\n")

import pandas
c= dir(pandas)
print(c)


# In[9]:


# File handling input and output
print("heloo")

var1 = open("file.txt","w")
print(var1)
print(var1.name)

var1.write("omesh kumar is a good boy, he want to become WBTCH")

var1.close()

var2 = open("file.txt","r+")
var3 = var2.read(5)            # value put in read function is tell about how much character you want
print(var3)
var2.close()

# to make directory and change the name of file

import os
# os.mkdir("hi")
# os.mkdir("hii")
# os.rename("hi","bye")
# os.remove("file.txt")      # this can't delete directory


# In[1]:



print("manoj")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


a


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




