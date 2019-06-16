from __future__ import print_function
import random
''' PROCEDURE '''

#1. N/A

#2. N/A

#3. N/A

''' Part I: Tuples, Syntax '''

#4. (1, 2, 3) 

'''
5. My english teacher requires MLA formatting for our essays. Mr.Brown has not
stated any specific conventions for variable at the moment.
'''

'''
6a. It will return 'b' because the index of 1 really means the second item in 
the tuple.

6b It will return ('a', 'b') because the index of two will be excluded and it 
will return the values at index 0 and 1.
'''

'''
7a. It returns true because the b[1] is equal to 10 which is equal to itself.

7b. It returns 15 because the last assigned value to a was 15 so it overrides
the variable and displays its value.
'''


''' Part II: Lists '''

#8. It displays all values at index one and beyond so ['b', 3]

#9. It returns false because the integer 3 is no the same as the string 3.

'''
10a. It will return ['a', 'b', '3', 4, 5] because the new values were just
concactenated on to the end of the list.

10b. It will return ['a', 'b', '3', 4, 5, [6, 7]] becuase it will add the new
values to the end of the list and it will have brackets because you don't need
them when using append.
'''

#11. This would not work because the list would not know what datatypes to add.

'''
12.This would return 18 because it would do 6*3 and then set itself equal to 
the product.
'''


''' Part III: Lists and the random module '''

'''
13. Tested the functions.
'''

'''
14. Code Below
'''

def roll_two_dice():
    '''
    Chooses two numbers between one and six and adds them.
    Outputs the sum of the two numbers
    Takes no input
    '''
    roll_One = random.randint(1,6)
    roll_Two = random.randint(1,6)
    output = roll_One + roll_Two
    return output
    
''' CONCLUSION '''

'''
1. They are all different data types with their own specific sets of rules. Like
how tuples cant be directly changed after they are defined and how a list has to
be between brackets.
'''

'''
2. To allow for variety and more uses in the langauge. Having only one type of 
variable would not be useful for the coder.
'''

'''
3. I learned multiple data types, strings, integers, floats, booleans, lists,
tuples, and more. I learned about functions, loops, and if statements, and how 
to use them with proper syntax. I also learned about the print function.
'''

''' ASSIGNMENT CHECK '''

'''
1. I recieved the output from my dice roll function so I think I did everything
correctly.
'''

#1.3.6 Function Test
print(roll_two_dice())
