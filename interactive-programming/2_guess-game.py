# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

# initialize global variables
secret_number = 0
guess_number = 0
range_num = 100

# helper function to start and restart the game
def new_game():

    global secret_number
    global guess_number
    global range_num
    #select a random number
    secret_number = random.randrange(0, range_num)
    guess_number =int(math.ceil(math.log(range_num+1, 2)))
    print
    print "New game. Range is [0,"+ str(range_num) + ")"
    print "Number of remaining guesses is ", + guess_number
new_game()


# define event handlers for control panel
def range100():
    #set new range to 100, and start new game 
    global range_num
    range_num = 100
    new_game()

def range1000():
    #set new range to 1000, and start new game
    global range_num
    range_num = 1000
    new_game()
    
def input_guess(guess):

    global secret_number
    global guess_number
    global range_num
    
    #print input number
    input_num = int(guess)
    print
    print "Guess was ", + input_num
    
    #print remaining guess number
    guess_number -= 1
    print "Number of remaining guesses is ", + guess_number
    
    #if guess number out of range, print error message
    if guess_number < 0 or guess_number >= range_num:  
        print "You ran out of guesses.  The number was ", + secret_number
    
    #compare input number and secret number
    if input_num == secret_number:
        print "Correct!"
        print " "
        new_game()    
    elif input_num > secret_number:
        print "Lower!"     
    else:
        print "Higher!"


    

frame = simplegui.create_frame('Guess the Game', 200, 200)
frame.add_input( "Enter a guess", input_guess, 200)
frame.add_button("Range is [0, 100)",  range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.start()

#http://www.codeskulptor.org/#user41_kB8Vq31cMk_1.py