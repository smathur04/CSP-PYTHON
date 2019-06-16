################################################################################

def hangman_display(guessed, secret):
    
    '''
    This function takes the arguments of a string input of letters(guessed) 
    and a string which contains a secret word(secret)
    It outputs/returns the string a hangman player would see with the letters in
    the secret word that they haven't guessed being dashes and the ones they got
    correct in their guess being revealed.
    In this function it looks at every character in secret and adds it to 
    dis_secret as a letter, dash, or empty space.
    '''
    
    #Display Variable
    dis_secret = ''
    
    #Loops through each character inside secret
    for char in secret:
        
        #If the character was guessed it will be revealed in the display
        if char.lower() in guessed or char.upper() in guessed:
            dis_secret += char
        
        #Blank spaces will stay as blank spaces    
        elif char == ' ':
            dis_secret += ' '
        
        #Letters that were not guessed become dashes    
        else:
            dis_secret += '-'

    #Outputs the display variable
    return dis_secret

################################################################################

def hangman():
    
    '''
    This function takes no arguments when it is called but does require the
    player to input a one letter guess or (if they know it) the entire secret
    word. Also, the player has to input yes or no when asked if they want to
    play again or continue moving on to the next word.
    
    It does not return anything because we have coded it to print the outputs.
    This function prints out the players' turns left, the secret word, 
    raw_input prompts for the player to guess a letter or whole word, a winning 
    message, a game over message, and a raw_input prompts on whether they want 
    to restart (there is also a prompt for if they want to continue playing)
    
    This function prompts the player to guess one letter or the whole word from
    a list of four secret food related words words. If they guess one letter it 
    continues the same process until they get the whole word and then moves on. 
    If they guess the whole word it moves on, but they must get it exactly right
    (not case sensitive). If they try to cheat and guess multiple random letters 
    it reprompts them to guess again and removes a turn. Theses cycles continue
    till they are out of turns, the win, or if they choose to stop playing.
    Also the player can choose to restart the game when they run out of turns. 
    And they can choose whether or not they would like to keep playing and move
    on to the next word after getting a word correct.
    '''
    
    #This is the 'rolling sum' of the guesses and new_guesses are added to it
    guessed = ''
    
    #Used to iterate through foods so each word is asked once
    secret_word_index = 0
    
    #List of foods the player has to guess
    foods = ['Apple Pie', 'Ice Cream', 'Sausage', 'Sushi']
    
    #The number of turns/tries that the player has
    turns = 7

    #Prints the introduction and rules
    print
    print '------------------'
    print 'WELCOME TO HANGMAN'
    print '------------------'
    print
    print 'YOUR THEME IS ... FOOD!'
    print
    print '''You get 7 total turns per word to guess four food-related words.'''
    print '''If you run out of turns, then it is GAME OVER!'''
    print 'Remember to guess one letter at a time!'
    print 'Also, both uppercase and lowercase works!'
    print 'If you think you know the word, then guess the whole word.'
    
    #This lets the player guess the word as long as they still have tries left
    while turns > 0:
        
        #Prints out the secret word with dashes and the guessed letters revealed
        print
        print hangman_display(guessed, foods[secret_word_index]) 
        print foods[secret_word_index]
        print
        
        #Prints hints for each word
        if secret_word_index == 0:
            print 'Hint: A baked pastry that goes great with Ice Cream'
        elif secret_word_index == 1:
            print 'Hint: A sweet, cold treat on a hot day!'
        elif secret_word_index == 2:
            print 'Hint: Popular breakfast item made of meat'
        elif secret_word_index == 3:
            print 'Hint: A very famous Japanese dish.'
            
        #Prompts the player to guess a letter or the whole word if they know it
        print
        new_guess = raw_input('Guess a letter that is in the hidden word\
 above or try and guess the whole word: ')
        
        #This loop runs only if the player's guess was longer than 1 letter
        while len(new_guess) > 1:
            
            #Runs when the any word other than the last is guessed correctly
            #Is not case sensitive
            if new_guess.lower() == foods[secret_word_index].lower() and \
            secret_word_index < 3:
                print
                print 'Congratulations! You guessed the word correctly!'
                print "Would you like to move on to another word?"
                replay = raw_input('Yes or No? ')
                if replay in ['yes', 'Yes', 'y', 'Y']:
                    turns = 8 #
                    secret_word_index += 1 #Moves to the next food in the list
                    guessed = '' #Resets all guessed letters
                    new_guess = '' #Resets the new_guess
                elif replay in ['no', 'No', 'n', 'N']:
                    return
                else:
                    print "You didn't choose either."
                    return
            
            #Player wins if they guess the last word correctly
            elif new_guess.lower() == foods[secret_word_index].lower() and \
            secret_word_index == 3:
                print
                print 'You Win!'
                return #Used instead of break to restart the loop 
            
            #If the player did not guess the word and their guess was more than
            #one letter than they are prompted again with one turn lost
            else:
                turns += -1
                
                if turns == 0:
                    print "You ran out of turns! Game Over!"
                    break
                
                else:
                    print 'You have ' + str(turns) + ' guesses left'
                    print
                    new_guess = raw_input('Guess ONLY ONE LETTER that is in the\
 hidden word above or guess the whole word CORRECTLY: ')
                    print
        
        #Adds the newest guess to the rolling sum and removes a turn     
        else:
            guessed += new_guess 
            turns += -1 
        
        #Checks if the word is not fully guessed and if not print their turns
        if '-' in hangman_display(guessed, foods[secret_word_index]):
            print 'You have ' + str(turns) + ' guesses left'
            print
        
        #If the entire last word has been guessed the player wins
        elif '-' not in hangman_display(guessed, foods[secret_word_index]) and\
        secret_word_index == 3:
                print
                print 'You Win!'
            
        #If the word is not the last word and it is fully guessed then move on
        else:
            print
            print hangman_display(guessed, foods[secret_word_index]) 
            print
            print 'Congratulations! You guessed the word correctly!'
            print "Would you like to move on to another word?"
            replay = raw_input('Yes or No? ')
            if replay in ['yes', 'Yes', 'y', 'Y']:
                turns = 8 #
                secret_word_index += 1 #Moves to the next item in the food list
                guessed = '' #Resets all guessed letters
                new_guess = '' #Resets the new_guess
            elif replay in ['no', 'No', 'n', 'N']:
                return
            else:
                print "You didn't choose either."
            
    
    #If you run out of tries then it prints game over and ends the game
    else:
        print "You ran out of turns! Game Over!"
        print "Would you like to play again?"
        replay = raw_input('Yes or No? ')
        if replay in ['yes', 'Yes', 'y', 'Y']:
            hangman()
        elif replay in ['no', 'No', 'n', 'N']:
            return
        else:
            print "You didn't choose either."
            
################################################################################

hangman()

################################################################################