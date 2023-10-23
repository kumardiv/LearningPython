#alt + shift + down array to copy paste lines

import pandas
import hashlib

# Comments ctrl + /

'''
Multi
Line
Comment
'''

# \ is an escape sequence character

print("Hello My \"name is Divesh\" \n and I am a Software Developer")
print(5)

print("Divesh", 5, 6, sep="-", end=None)

print("Hello")

a=1

print(a)

b="Divesh"

print(b)

print(type(a))

#list - mutable
#tuple - immutable
#dict - mutable
#string - immutable

# // floor division operator

print(15//6)

# Exponential operator
print(2**4)

# It takes input as string
# n = int(input("Enter first number: "))
# m = int(input("Enter second number: "))
# print(n+m)

name = "Divesh"

#name = 'Divesh'

apple = 'He said, "I want to eat an apple"'

print(apple)

# Also works with double quotes
string = '''Hello
My
Name
is
Divesh
'''

print(string)

string1 = "Divesh"

for ch in string1:
    print(ch, end='')

#String slicing
name2 = "Divesh Kumar"
print(name2[0:5])

print(len(name2))

# Automatically include 0
print(name2[:5])

# Automatically include length of name
print(name2[1:])

print(name2[0:-1])

print(name2[-3:-1])

namee = "Harry"

print(namee[-4:-2])

string2 = "DIVESH!!!!!"

print(string2.lower())

print(string2.upper().rstrip("!"))

#Remove trailing character
print(string2.rstrip("!"))

print(string2.replace("DIVESH", "KUMAR"))

# Created a list of elements separated by space
print(name2.split(" "))

heading = "introduction to python"

# Make first letter capital
print(heading.capitalize())

title = "Welcome"

# Centre align using specified character, default is space
str1 = "Welcome to the Console!!!"
print(str1)
st = str1.center(100, "*")
print(st)

# Count number of occurances
st1 = "Divesh Hello Hi Divesh Hi!!!"
print(st1.count("Divesh"))

print(st1.endswith("!!!"))

print(st1.endswith("sh", 0, 6))

# Find the number of occurances

print(st1.find("Hi"))

# Returns -1
print(st1.find("Hii"))

# Similar to find method, but it raise exception

print(st1.index("Hi"))

str1 = "WelcomeToTheConsole"
print(str1.isalnum())
str1 = "Welcome"
print(str1.isalpha())

str1 = "hello world"
print(str1.islower())

# If character is printable
str1 = "We wish you a Merry Christmas\n"
print(str1.isprintable())
str1 = "         "       #using Spacebar
print(str1.isspace())
str2 = "  "       #using Tab
print(str2.isspace())

str1 = "World Health Organization" 
print(str1.istitle())

str2 = "To kill a Mocking bird"
print(str2.istitle())

str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))

str1 = "Python is a Interpreted Language" 
print(str1.swapcase())

str1 = "His name is Dan. Dan is an honest man."
print(str1.title())

#The istitle() method returns True if all words in a text start with a upper case letter, AND the rest of the word are lower case letters, otherwise False.

var=10
if(var < 5 and var > 20):
    print("True")
elif(var > 5 and var < 20):
    print("Hello")

var1 = int(input("Enter the number"))

match var1:
    case 0:
        print("Number is 0")
    case 1:
        print("Number is 1")
    # Default case
    case _:
        print("Default case")


x = int(input("Enter a number"))
match x:
    case 0:
        print("Number is 0")
    case 1:
        print("Number is 1")
    # Default case
    case _ if(x!=4):
        print("Default case")
    case _ if(x==5):
        print("Number is 5")
    case _:
        print("No match")

