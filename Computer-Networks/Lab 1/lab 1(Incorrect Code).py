#!/usr/bin/python

import sys
#import hello
import time



print("Hello World");
print ("Hello World");
#print "Hello World"
#print 'Hello World'
#print "Hello World"; print 'How are u'





x=10
print (x)
print (x**2)
x='Hello'
print (x)


str = 'Hello World!'
print (str) # Prints complete string
print (str[0]) # Prints first character of the string
print (str[2:5]) # Prints characters starting from 3rd to 5th
print (str[2:]) # Prints string starting from 3rd character
print (str * 2)# Prints string two times
print (str + "TEST") # Prints concatenated string

#Always string returned in raw_input (input since 3.0)
y=raw_input("Pl enter any value: ")
print (y)
print (5*y)
print (5*int(y))
#Command line arguments 
print (str(sys.argv))
print (len(sys.argv))
print (int(sys.argv[1]))
#Lists vs Tuple Vs Dictionary
#list
list1 = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
print (list1) # Prints complete list
print (list1[0]) # Prints first element of the list
#print list1[1:3] # Prints elements starting from 2nd till 3d
#print list1[2:] # Prints elements starting from 3rd element
#list1[2] = 1000 # Valid syntax with list
#print list1

#Tuple
#list2 = ( 'abcd', 786 , 2.23, 'john', 70.2 )
#list2[2] = 1000 # In-valid syntax with tuple

#Dict
#list3 = {'EmpName': 'Ahmed','EmpCode':6734, 'Dept': 'sales'}
#print list3['EmpName'] # Prints value for 'one' key
#print list3['Dept'] # Prints value for 2 key
#print  list3 # Prints complete dictionary
#print list3.keys() # Prints all the keys
#print list3.values() # Prints all the values

#Decisions
#x=10
#y=20
#if (x<11):
#    print 'value of x is: ',x
#    print 'value of x is: ',x
#elif (y<11):
#	print 'value of y is: ',y
#else:
#	print "None is true"

#Loops
#x=10
#while(x>5):
#	print x
#	x=x-1

#y=[1, 2, 5]

#for Loop
#for x in y :
#	print x

#list=['Hello', 1, 2, "End"]
#for x in list:
#	print x


#Functions
#def myfunction(*arg):
#	print arg
#	for n in arg:
#		print int(n)

#myfunction(10,20,30)
#myfunction(40)

#External functions
#hello.print_it(100)


#Files
#myFile=open("hello.py")
#data=myFile.read();
#print data
#myFile.close();


#print " Current time: ", time.asctime(time.localtime(time.time()))
#print sys.path

