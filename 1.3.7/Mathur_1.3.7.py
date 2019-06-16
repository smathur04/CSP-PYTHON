from __future__ import print_function
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import random


''' PROCEDURE '''

#1. N/A

#2. N/A

#3. N/A

''' Part I: for loops, range(), and help() '''

def days():
    '''
    This function prints an abrreviated version of each day in the week on indi-
    vidual lines and prints a line for the 5th, 6th, and 7th of december.
    It takes no input
    Outputs/Prints days of the week and days in September.
    '''
    for day in 'MTWRFSS': 
        print(day + 'day')
    for day in range(5,8):
        print('It is the ' + str(day) + 'th of September')

'''
4. Docstring Above 
'''

def picks():
    '''
    This function makes a histogram called picks from a list which contains 6
    numbers that are either 1, 3, or 10.
    Takes no input
    Creates a new .png file with a histogram in it.
    '''
    a = [] # make an empty list
    # Why all the brackets below? 
    # a += [  brackets here to add an iterable onto a list]
    #    random.choice(   [brackets here to choose from a list])

    a += [random.choice([1, 3, 10])]
    for choices in range(5):
        a += [random.choice([1, 3, 10])]

    plt.hist(a)
    plt.savefig('1.3.7/picks')

'''
5. Code Above
'''

def roll_hundred_pair():
    '''
    This is a function that produces a histogram of the results of 100 rolls of 
    two 6-sided dice
    Takes no input
    Creates a new .png file with a histogram in it.
    '''
    individual_rolls = []
    
    for rolls in range(1, 101):
        dice_one = random.randint(1,6)
        dice_two = random.randint(1,6)
        individual_rolls.append(dice_one + dice_two)
    
    plt.hist(individual_rolls)
    plt.savefig('1.3.7/rolls')
    
    
    
def dice(n):
    '''
    This is a function that returns the sum of a random roll of n 6-sided dice.
    Takes an input, 'n' that is an integer which decides how many dices will be
    rolled
    Outputs/Prints the sum of all the dice rolls.
    '''
    
    sum_of_dice_rolls = 0
    
    for i in range(0, n):
        roll = random.randint(1,6)
        sum_of_dice_rolls += roll
        
    print (sum_of_dice_rolls)
    return sum_of_dice_rolls
    
'''
6. Code Above
''' 


'''Part II: While loops'''



def validate():
    '''
    This function asks you to name a letter in the words 'hangman word' if you 
    get it correct then it syas thank you and stops running but getting it wrong
    will make it ask you again.
    Takes no input
    Prints 'thank you!' and a question prompt
    '''
    guess = '1' # initialization with a bad guess
    answer = 'hangman word'
    while guess not in answer:
        guess = raw_input('Name a letter in \''+answer+'\': ')
    print('Thank you!')

'''
7. Line 2 is nessecary, because unlike for loops, while loops don't initialize a
variable by themselves and need the variable to initialized eariler in the code.
Also, if guess was 'a' then the loop would never start and if line 2 was not
there the loop would not start.
'''


def guess_winner(players=('Amy', 'Bill', 'Cathy', 'Dale')):
    '''
    This is a function that lets you choose a name from four names and if the
    lottery winner is the name you pick, you win. If you pick wrong then you
    guess until you are correct. It also prints your number of guesses.
    
    When calling the function you don't need arguments or any input because the
    four players names (strings) are already defined in the function as the
    input. 
    
    The function outputs the integer value of the number of guesses it took you
    to guess the lottery winner.
    '''
    
    winner = random.choice(players) 

    ####
    #Asks you to guess a name from the four names it prints out.
    ####
    print('Guess which of these people won the lottery: ',end='')
    for p in players[:len(players)-1]:#Index is becomes 0:3 only prints 3 names
        print(p+', ', end='')   
    print(players[len(players)-1])#Prints out the last name in the list (Dale)

    ####
    #Tells you to guess again / prints winning message & outputs number of tries
    ####
    guesses = 1 
    while raw_input() != winner:
        print('Guess again!')
        guesses += 1
    print('You guessed in', guesses, 'guesses!')
    return guesses    

'''
8. DOCSTRINGS ABOVE
'''

def goguess():
    '''
    This function prompts the user keep guessing a number between 1 and 20 until
    they get it correct.
    Takes no input
    Prints a winning message and your number of guesses.
    '''
    turns = 1
    secret_number = random.randint(1, 20)
    guess = raw_input('I have a number between 1 and 20 inclusive. Guess: ')
    
    while str(guess) not in str(secret_number):
        
        if float(guess) > float(secret_number):
            print(guess, 'is too high.')
            turns += 1
            
        else:
            print(guess, 'is too low.')
            turns += 1
            
        guess = raw_input('I have a number between 1 and 20 inclusive. Guess: ')
        
    else:
        print('Right! My number is', secret_number, '!', 'You guessed in', turns,
        'guesses!')
        return 
    
'''
9. Code Above
'''

'''
10. It will take 12 guesses if you use decimals, because you can reach a
correct answer after dividing your range by 2 twelve times. 
'''


''' Part III: Practice '''

def matches(ticket, winners):

    '''
    This is a function that takes two lists and returns an integer that says 
    how many numbers the two lists have in common.
    Takes two lists as input
    Outputs how many numbers they have in common.
    '''
    
    number_of_matches = 0
    
    for i in range(0, len(ticket)):
        if str(ticket[i]) in str(winners):
            number_of_matches += 1
    
    return number_of_matches
    
'''
11a. CODE ABOVE!
'''    

def report(guess, secret):
    
    '''
    This is a function that takes two lists and returns a 2-element list 
    [number_right_ place, number_wrong_place], it simulates a game of mastermind
    Takes two lists as input
    Returns a 2 item list
    '''
    
    right_wrong = [0, 1]
    already_added = []
    
    for i in range(0, len(secret)):
        
        if guess[i] == secret[i]:
            right_wrong[0] += 1
            
        elif guess[i] in secret and guess[i] != secret[i]:
            right_wrong[1] += 1
            already_added.append(guess[i])
            if guess[i] in already_added:
                right_wrong[1] -= 1
            
    return right_wrong
         
'''
11b. CODE ABOVE!
'''

''' CONCLUSION '''

'''
1. It would be insanely time consuming if you are making a complicated program
and with that much extra, unnessacery code you leave room for lots of errors, as
conditionals need to have perfect logic to work. Also, it will make the program
a lot slower and more confusing to code.a

2. With iteration you can change, replcace, add, or remove things from data but
with analysis you can just review and re-look at that data. 

3. While loops only run when the conditional statement following them is TRUE
and can't initialize variables on their own. For loops initialize variables
within themselves and can be edited to loop only a certain number of times.
While loops are more similar to conditional statements rather than for loops.

4. My partner and I worked pretty well together, but I think we should have
communicated a little more. Instead of talking to each other when we were stuck
or needed clarification, we should have discussed a little after every question.
'''

''' ASSIGNMENT CHECK '''

roll_hundred_pair()
dice(5)
print (matches([11, 12, 13, 14, 15], [3, 8, 12, 13, 17]))
guess = ['red','red','red','green','yellow']
secret = ['red','red','yellow','yellow','black']
print (report(guess, secret))
goguess()

''' I believe I successfully finished the assignment!'''

