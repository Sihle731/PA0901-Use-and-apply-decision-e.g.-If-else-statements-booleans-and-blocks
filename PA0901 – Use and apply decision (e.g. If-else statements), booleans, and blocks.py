'''Exercise 1
Create a program that checks if a number is positive or negative.'''

def integer(number):
    if number < 0:
        print('The number is Negative')
    else:
        if number >= 0:
            print("The number is positive")

integer(-7)

'''
Exercise 2
Create a program that checks if someone can vote (18+).'''

def eligible_vote(age):
    if age < 18:
        print("Voter is a minor, not eligible to vote")
    else:
        if age >= 18:
            print("Voter is an Adult, and is eligible to vote")

eligible_vote(31)

'''
Exercise 3

Create a program that:

Prints "High" if number > 100
Prints "Medium" if number is between 50 and 100
Prints "Low" otherwise'''

def num_level(number):
    if number > 100:
        print("High")
    else: 
        if 100 > number >= 50:
            print("Medium")
        else:
            print("Low")

num_level(34)

'''
Exercise 4
Create a Boolean variable called isMember.

If true → print "Discount applied".
If false → print "No discount".'''

is_Member = True

def price(member):
    if member == False:
        print("No discount")
    else:
       print("Discount Appiled")

price(is_Member)
