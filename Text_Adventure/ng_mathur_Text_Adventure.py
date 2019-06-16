################################################################################

from sys import exit
import random

################################################################################

def end():
    '''
    Takes no input
    Function to stop running the code when the player dies or makes a mistake
    Prints Game Over
    '''
    
    print 'Game Over'
    exit(0)
    
################################################################################

def intro():
    '''
    Function that runs the scenes before entering the actual maze.
    Takes no input
    It prints startup text, asks your name, responds with a greeting, asks to 
    start the game, and starts the story
    '''
    
    #Starting Text
    print 
    print '-----------------------'
    print 'ENTER THE MAZE OF DEATH'
    print '-----------------------'
    print 
    
    #Asks Your Name
    name = raw_input('What is your name?: ')
    
    #Greets You
    print
    print 'Hello ' + str(name)
    
    #Asks you to start the game
    begin = raw_input('Type start to begin: ')
    
    #Maze Enterance Text prints if you type start
    if begin in ['start', 'Start', 's', 'S', 'START']:
        print 
        print 'You walk in to the maze and it starts closing behind you'
        print
    
    #If start is not typed this prints
    else:
        print 
        print 'Well you did not start the game so what do you expect?'
        print
        end()
        
intro()

################################################################################

def s1():
    '''
    Function for the first scene of the maze game, it asks if you should run out
    of the maze before it closes or not
    Takes no input
    Only prints what happens depending on what the player types in the terminal
    '''

    #Asks you if you should go back out or not
    goback = raw_input('Do you run back out before it closes? Yes or No: ')
    
    #If you pick yes the game ends
    if goback in ['yes', 'Yes', 'Y', 'y']:
        print
        print 'You got stuck betwen the closing walls of the maze and died'
        end()
    
    #If you pick no then you continue playing
    elif goback in ['no', 'No', 'N', 'n']:
        print
        print 'Smart choice, you continue to walk forward, deeper into the maze'
        print
    
    #If neither option is chosen the game ends
    else: 
        print
        print 'You did not choose Yes or No'
        print
        end()

s1()

################################################################################

#Asks if you go left, right, or straight in the maze
fork = raw_input('You aproach a fork in your path, do you go left, right or\
 straight? ')

################################################################################

def go_straight():
    '''
    Takes no input
    This is the function for when the player chooses to go straight, it also
    includes the code for the result of them going straight (the player dies)
    Prints the death message and game over
    '''
    
    #If you choose to straight then you die
    if fork in ['s', 'S', 'straight', 'Straight']:
        print
        print 'Without looking, you step forward into a lava pit and DIE! '
        print
        end()

################################################################################

def go_left():
    '''
    Takes no input
    This is the function for when the player chooses to go left and it includes
    all the decisions and code for what happens after going left
    Prints various massages depending on what the player types in the terminal
    '''
    
    #Choosing left allows you to survive and keep playing
    if fork in ['l', 'L', 'left', 'Left']:
        print
        print '''You walk into the left hallway and see a lever'''
        print
        
        #Asks if you should pull the lever
        lever =  raw_input('''Do you pull the lever? Yes or No: ''')
        
        #Pulling the lever makes you fall through the floor
        if lever in ['y', 'Y', 'Yes', 'yes']:
            print
            print 'The ground below you vanishes and you fall into a dark room'
            print
            print '''You feel around and touch something round'''
            print
            
            #Asks if you should pick up the object
            ball = raw_input('Do you pick it up? Yes or No: ')
            
            #Picking it up causes the game to end
            if ball in['y', 'Y', 'Yes', 'yes']:
                print
                print '''THE BALL IS BOMB! You accidently detonate it and it
                explodes in your hands!'''
                print
                end()
            
            #Not picking it up lets you win the game    
            elif ball in ['n', 'N', 'No', 'no']:
                print
                print 'You decide not to pick it up and an exit door appears!'
                print 'YOU WIN!!!!!!'
            
            #Didn't choose either option for picking up the object    
            else:
                print
                print 'Next time try to choose yes or no!'
                end()
                
        #Not pulling the lever also ends the game         
        elif lever in ['n', 'N', 'No', 'no']:
            print
            print 'You do not pull it and just stand there FOREVER!'
            end()
            
        #Didn't chose either option for pulling the lever 
        else:
            print 'Next time try to choose yes or no!'
            end()

################################################################################

def go_right():
    '''
    Takes no input
    This is the function for when the player chooses to go right and incluedes
    all the code for what happens/what decisons are made after going right
    Prints several things depending on what decisions the player makes
    '''
    
    #Going right allows the player to keep playing and enter the right hallway
    if fork in ['r', 'R', 'right', 'Right']:
        print
        print 'Great Choice! You enter a narrow hallway and see a bucket with\
 ten pieces of candy in it that says take one on it'
        print
        
        #Asks how much candy (out of 10) the player wants to take
        candy = raw_input('How much candy do you take? Please write the number\
 amount you want: ')
        print
    
    #If they take 1-5 they die
    if candy in ['1', '2', '3', '4', '5']:
        print 'No normal person takes that little candy!'
        print 'Candy rains from the ceiling and you are suffocated by it!'
        end()
    
    #Taking 6-10 lets them live and enter the serpent's hallway
    elif candy in ['6', '7', '8', '9', '10']:
        print
        print
        print
        print
        print 'Good Job! Nobody ever takes only one. What was once a dead end\
 now opens up into a large hallway'
        print
        print 'In the hallway there is a large serpent gaurding the maze exit!'
        print
        print 'Serpent: I am going to think of a number between 1 and 4 and if\
 you get it correct you can leave but if you get it wrong. LUNCHTIME!!'
        print
        
        #Variable that is the serpents random number
        rando = random.randint(1,4)
        
        #Asks the player to guess the number that the serpent is thinking of
        slimey = raw_input('NOW PICK A NUMBER BETWEEN 1 AND 4: ')
        
        #The player wins if they guess correctly
        if slimey in str(rando):
            print 'Serpent: I did not think you could, but you did it!'
            print 'YOU WIN!!!!!!'

        #The player dies if they guess wrong
        else:
            print 'Serpent: LOL LUNCHTIME!'
            end()
    
    #The game ends if they don't choose 1-10 pieces of candy
    else:
        print "That isn't even an option, there is only 10 pieces in the bowl!"
        end()

################################################################################

#This will run the go_straight function only if the player chose to go straight
if fork in ['s', 'S', 'straight', 'Straight']:
    go_straight()

#This will run the go_left function only if the player chose to go left
elif fork in ['l', 'L', 'left', 'Left']:
    go_left()

#This will run the go_right function only if the player chose to go right  
elif fork in ['r', 'R', 'right', 'Right']:
    go_right()

#This will end the game if none of the options were typed in to the terminal
else:
    print 'Please only type an answer from the choices provided!'
    end()
    
################################################################################