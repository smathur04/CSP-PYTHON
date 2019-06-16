from __future__ import print_function
import random 
'''Part I. Nested if structures and testing'''

def food_id(food):
    ''' Returns categorization of food

    food is a string
    returns a string of categories
    '''
    # The data
    fruits = ['apple', 'banana', 'orange']
    citrus = ['orange']
    starchy = ['banana', 'potato']

    # Check the category and report
    if food in fruits:
        if food in citrus:
            return 'Citrus, Fruit'
        else:
            return 'NOT Citrus, Fruit'
    else:
        if food in starchy:
            return 'Starchy, NOT Fruit'
        else:
            return 'NOT Starchy, NOT Fruit'

'''
1a. The return output resulted from line 17.
'''

'''
1b.
I: The input of food_id('orange')
II: The input of food_id('apple')
III: The input of food_id('potato')
IV: The input of food_id('carrot')
'''

'''
1c. This is because the code runs top to bottom so the banana would be given the
output 'NOT Citrus, Fruit' before it could reach the starch if/else statement.
'''

'''
2. Everything works as expected!
'''

def food_id_test():
    ''' Unit test for food_id
    returns True if good, returns False and prints error if not 
    good
    '''
    works = True
    if food_id('orange') != 'Citrus, Fruit':
        works = 'orange bug in food id()'
    if food_id('banana') != 'NOT Citrus, Fruit':
        works = 'banana bug in food_id()'
    if food_id('apple') != 'NOT Citrus, Fruit':
        works = 'apple bug in food_id()'
    if food_id('potato') != 'Starchy, NOT Fruit':
        works = 'potato bug in food_id()'
    if works == True:
        print("All good!")
        return True
    else:
        print(works)
        return False

'''
3. Answer was as expected.
'''

def f(n):
    '''Number Guesser Game
    takes the input of n which can be any data type but code works with integers
    returns whether the number is odd, even, a mulitple of 6, or not an integer
    '''
    if int(n) == n:
        if n % 2 == 0:
            if n % 3 == 0:
                return 'The number is a multiple of 6'
            else:
                return 'The number is even'
        else:
            return 'The number is odd'
    else:
        return 'The number is not an integer'
        
'''
4. 
f('9')
f(3)
f(2)
f(12)
'''

'''
5. N/A
'''

def f_test():
    '''
    Test suite for f(n)
    Takes no input.
    Returns True if good, returns False and prints error if not 
    good
    '''
    
    works = True
    if f('9') != 'The number is not an integer':
        works = 'Integer Bug'
    if f(6) != 'The number is a multiple of 6':
        works = 'Multiple of 6 bug'
    if f(2) != 'The number is even':
        works = 'Even Bug'
    if f(3) != 'The number is odd':
        works = "Odd Bug"
    if works == True:
        print("All good!")
        return True
    else:
        print(works)
        return False
        
'''
7. When you use '+' with floats and integers then it is for numeric addition,
but when it is used with non numeric data types it is a concactination. 
'''
        
'''
8. Code Below
'''

def guess_once():
    '''
    Function that guesses a number between 1 and 4 inclusive.
    Takes raw_input that user types in IPYTHON shell
    Returns if the guess was correct, too low, or too high.
    '''
    secret = random.randint(1, 4)
    print('I have a number between 1 and 4.')
    guess = int(raw_input('Guess: '))
    if guess == secret:
       print('Right, on!', 'I was number', secret, end='!\n')
    elif guess > secret:
        print('Too high, my number was', secret, end='!\n')
    elif guess < secret:
        print('Too low - my number was', secret, end='!\n')
       
'''
8a. The end function makes the print be a string + a variable with a exlamation
mark on the end as oppossed to nothing
'''

'''
8b. Changed the program above.
'''

'''
9. Code Below
'''

def quiz_decimal(low, high):
    '''
    Function that tells you if a float is between two other floats
    Takes a low number input, a high number input, and the guess rawinput
    Returns if the number is in between the high and low or not
    '''
    
    print('Type a number between', float(low), 'and', float(high), ':')
    guess = float(raw_input('Guess: '))
    
    if float(low) < guess < float(high):
        print('Good!', float(low), "<", guess, "<", float(high))
    elif float(low) > guess:
        print('No,', float(guess), 'is less than', float(low))
    elif float(high) < guess:
        print('No,', float(guess), 'is greater than', float(high))
        
'''Conclusion'''
'''
1. Developers use glass-box testing to test if-structures.
'''

'''
2. Anywhere from 0 to all of them.
'''

'''
3. Test-suites help debug large functions, programmers might do them first to 
have more of a plan for what they need to do.
'''

'''
4. Yes; Code Below
'''

def even(n):
    if n % 2 ==0:
        return 'The number is even'
        
def odd(n):
    if n % 2 !=0:
        return 'The number is even'

def notint(n):
    if int(n) ==n:
        return 'The number is even'
        
def mult6(n):
    if n % 2 ==0 and n % 3 == 0:
        return 'The number is even'


print(food_id('apple'))
food_id_test()
f(1.1)
f(2)
f(3)
f(6)
f_test()
guess_once()
guess_once()
quiz_decimal(4, 4.1)
quiz_decimal(4, 4.1)
#f_challenge(1.1)
#f_challenge(2)
#f_challenge(3)
#f_challenge(6)
