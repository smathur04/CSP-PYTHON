from __future__ import print_function # use Python 3.0 printing



'''Procedure'''
#1-5 N/A




'''Part 1: Conditionals'''

'''6a Prediction: I think that the output would be true because evaluating the 
function with a = 3 would return true.'''
# My prediction was correct.

'''6b Prediction: I think that the output would be true because "true or true" 
would result in true.'''
# My prediction was correct.

#7 40<x and x<130 and 100<=y and y<=120

#8 Got true like I was supposed to.




'''Part II: if-else Structures & the print() Function!!!!'''

def age_limit_output(age):
    '''Determines the age limit of something and uses the age parameter to 
    output whether the limit was met or not'''
    AGE_LIMIT = 13          # convention: use CAPS for constants
    if age < AGE_LIMIT:
        print(age, 'is below the age limit.')
    else:
        print(age, 'is old enough.')
    print(' Minimum age is ', AGE_LIMIT)
    
'''9a. Predictions: The age of ten will print "is below the age limt" and 16 
will print "is old enough"'''
'''My prediction was correct because I plugged the arguments in the function in 
my head.'''

#9b. Code is below, it worked as expected.
def report_grade(percent):
    '''Determines if a student has reached mastery by seeing if the percent 
    parameter is over 80% and then prints text accordingly'''
    if percent <= 80:
        print("A grade of", percent, "does not indicate mastery.")
        print("Seek extra practice or help.")
    else:
        print("A grade of", percent, "indicates mastery.")
        print("Keep up the good work!")
        
        
        
        
'''Part III. The in operator and an introduction to collections'''
'''10. Prediction: The integer of three will return true but the string of three
will be false.'''
#My prediction was correct.

#11. Worked as expected.
def vowel(letter):
    '''Determines if the letter parameter's input is a vowel and returns true or 
    false'''
    vowels = 'aeiouAEIOU'
    if letter in vowels:
        return True
    else:
        return False
        
def letter_in_word(guess, word):
    if guess in word:
        return True
    else:
        return False
        
#12. Worked as expected
def hint(color, secret):
    '''Takes the color parameter and a list of colors in the secret parameter,
    and displays wether or not the color is in the sequence of colors'''
    if color in secret:
        print("The color", color, "IS in the sequence")
    else:
        print("The color", color, "IS NOT in the sequence")
        



'''CONCLUSION'''

'''1. The blocks of code indented after the colon in if , elif, and else blocks
are child elements of the non indented code above them. The if, elif, and else
are the parent blocks of code.'''

'''2. We learned about >, ==, >=, <, <=, +, -, *, /, %, **, and, or , not, in, 
and a new one that I found online was !=.'''

'''3. Ira is sort-of right because there is no need for double the code but it is not 
really slowing things down. Jayla is 100% right because the code would always have
to be changed in two places. Kayla's memory statement is not really useful unless
the program is already huge.'''



'''ASSIGNMENT CHECK'''
'''1. After running the code I got:

10 is below the age limit.
 Minimum age is  13
16 is old enough.
 Minimum age is  13
A grade of 79 does not indicate mastery.
Seek extra practice or help.
A grade of 85 indicates mastery.
Keep up the good work!
True
The color red IS in the sequence
The color green IS NOT in the sequence

Based on the result, I do think I succesfully completed the assignment.'''

#1.3.3 Function Test
age_limit_output(10)
age_limit_output(16)
report_grade(79)
report_grade(85)
print(letter_in_word('t', 'secret hangman phrase'))
secret = ['red','red','yellow','yellow','black']
hint('red', secret)
hint('green', secret)