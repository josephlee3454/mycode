#!/usr/bin/python3
import random
"""Guess the Number Game | Written by Joseph Lee"""

"""
• Randomly pick a number between 1 and 100
• User makes a guess
• If the guess is too low, game should return "Too low!" and user can guess again.
• Too high, return "Too high!" and guess again.
• Game ends when correct number is chosen.

NEW FEATURES:
    print the number of guesses it took to get the right answer.
    the user only gets 10 guesses :)
"""
turns = 10
guess_num = 1
user_input = int(input( "Pick a number between 1 and 100  " ))
rand_num = random.randint(1, 100)
while user_input != rand_num and turns != 0: 
    turns -= 1 
    guess_num += 1
    if user_input < rand_num:
        
        print("to low")
    if user_input > rand_num:
        print("to high")
        
    user_input = int(input("Please guess a different number"))
if turns != 0:
    print("Congrats you guessed the answer !!!!!!! it took you "  + str(guess_num) )
else: 
    print("you lost !!!! the real value is " + str(rand_num)) 
