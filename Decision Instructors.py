#place a hashtag in front of the line so that line won't execute
#this is referred to as a "comment"

'''
Line one of comment
Line two of comment
Line three of comment
'''

"""
Line one of comment
Line two of comment
Line three of comment
"""

'''

A condition is a comparison 
Conditions evaluate a boonlean value to be true or false
If the condition was true, the following "block" of code will run
A block of code is indented

COMPARISONS

> Greater than
< Less than
>= Greater than or equal to
<= Less than or equal to
== equal to
!= not equal to

'''

mark = int(input("Please enter your test mark"))

if mark >= 90:
    print ("You aced it!")

elif mark >= 70:
    print("You got a B!")

elif mark >= 60:
    print("Thats a C!")
    
elif mark >= 50:
    print("You barely made it!")
    
else:
    print("You failed!")

if (mark >= 0 and mark <= 100):
    print("You have a valid mark!") 
    
if (mark >100 or mark < 0):
    print("This is an invalid mark")