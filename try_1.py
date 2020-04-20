import random

def main():
    ''' This is the main method for this program. It should play hangman

        For this method, you should use the provided list of words (or make your own)
        and use it to call your chosenWord method to choose a word from the list to play with.
        Then initialize an empty set to keep track of previous guesses, initialize an int to zero to
        keep track of how many times the user misses a guess, then call the printHangman
        method and printWord method to show the initial status of the game.

        Once the initial setup is complete, you will need to loop through prompting the user
        for their guess, calling checkGuess, printHangman, and printWord until the user has
        guessed all the letters in the word or they have used all their guesses.

        Finally, you need to see if the user completed the word or ran out of guesses
        and display an appropriate message based on whether they won or lost.
    '''
    ##Your code here##
    print("Welcome to hangman") #Welcome the gamer to the dojo
    words = ["pineapple", "carrots", "watermelon", "bananas", "cheese", "radishes", "jello"] #list to contain possible words
    words=chooseWord(words) #needs to go here before print(words)
    print(words)#use to see what word is to check if working
    guesses=[] #needs to be a set
    misses=len(guesses)#is this right to keep track of misses?
    #start the loop that runs through the game
    while misses<=6:
        guess=input("Guess a letter: ")
        print(checkGuess(words,guess, guesses, misses))
        printWord(words, guesses)
              
    pass


def chooseWord(words):
    '''A simple function to choose one word out of a list of words

    This method should be very simple.  Just pick a random number corresponding
    to an index of the list and return the word at that location.

    Parameters:
        words: A list containing strings for the user to guess
        
    Return:
        a single string that the user will use to play
    '''

    ##Your code here##
    return (random.choice(words)) #return the chosen word
    pass



def checkGuess(words, guess, guesses, misses):
    ''' A function to check the users guess

    This function should first check if the users guess has already been guessed.
    If the user has already guessed a letter, you should show a message indicating
    that and not penalize the user.
    Then if the user has not already guessed the letter, you should add the guess to
    the guesses set and increase misses if the letter
    is not in the word (ignoring case).
    
    Parameters:
        word: A string representing the word the user is trying to guess
        guess: A string representing the letter the user has guessed
        guesses: A set containing strings representing the letters the user has guessed
        misses: An int representing how many times the user has guessed incorrectly

    Return:
        tuple (set, int):
            set is the set of all previous guesses
            int is how many times the user has guessed incorrectly  
    '''
    ##Your code here##
    #establish the variables so hopefully there are no errors with those:)
    tmpwords=words 
    tmpguess=guess
    tmpguesses=guesses #needs to be a set
    tmpmisses = misses
    
    #see if guess has already been guessed then provide feedback
    if tmpguess in tmpguesses:
        print ("That has been guessed. Try again.")
    #if guess is in the word add it to guesses, print yes and the guesses so far
    elif tmpguess in tmpwords:
       #add tmpguess to tmpguesses
        tmpguesses.append(tmpguess)
        print("yes", tmpguesses)
    # if guess is not in word add 1 to misses based on the length of guesses, add guess to guesses, print not a letter.
    else:
        tmpmisses+=1
        #add tmpguess to tmpguesses
        tmpguesses.append(tmpguess)
        print ("That is not one of the letters.")
        
    return (tmpguesses, tmpmisses)
    pass



def printWord(words, guesses):
    '''A function to print the current word state for the user

        This function should generate and print a hangman representation of a word for the user.
        If the character in the word is not a letter A-Z, the character should simply be
        put in the representation shown to the user.  If the character in the word has already
        been guessed, it should also be put in the representation shown to the user.  If the character
        in the word has not been guessed yet, an underscore (_) followed by a space should be put in
        the representation shown to the user.  And finally, this method will return True if the user
        has successfully guessed the entire word or False if they need to keep guessing letters to
        fill in the word.

    Parameters:
        word: A string representing the word the user is trying to guess
        guesses: A set containing strings representing the letters the user has guessed

    Return:
        Boolean: either True or False representing if the user has guessed the entire word
        
    '''
    
    ##Your code here##
    #Establish variables
    tmpwords = words
    tmpguesses = guesses
    #create the string
    guessedWord = ""
    for i in tmpwords:
        if i in tmpguesses:
            guessedWord += i
    #Have underscore and space so they see the number of letters?
        else:
            guessedWord += "_ "
    print(guessedWord)        
    return guessedWord
    pass


def printHangman(misses):
    """ This method will show the current status of the game

        If you do not want to attempt the full method, you may simply print
        "You have missed X times out of 6" where X is replaced with how times
        the user has missed.
        
        **CHALLENGE**For the Challenge portion of this method, you will need to print the
        typical hangman graphic associated with the number of misses the user has.
        This should start with the head for the first miss, followed by the body
        for the second miss, followed by one of the legs for the third miss,
        followed by the other leg for the fourth miss, followed by one of the arms
        for the fifth miss, followed by the other arm for the sixth miss.  This is
        not overly difficult, but will take some time to get right.
        

    Parameters:
        misses: an int representing how many incorrect guesses the user has made.
    """
    ##Your code here##
    #Not sure where this goes in the loop
    #Does this go in another function?
    tmpmisses = misses
    print ("You have misses", tmpmisses, "out of 6") #Only 6 tries to hang the man
    pass



main()

