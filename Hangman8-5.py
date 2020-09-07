#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 11:55:00 2020

@author: apple
"""
import random
print('H A N G M A N')
random.seed()
word_list = ['python', 'java', 'kotlin', 'javascript']
guess = random.choice(word_list)
length = len(guess)
init = '-'*length
i = 0
print(init)
for i in range(8):
    letter = input('Input a letter: ')
    if letter in guess:
        for i in range(length):
            if letter == guess[i]:
                init = list(init)
                init[i] = letter
        print(''.join(init))
    else:
        print('No such letter in the word')
    
    i += 1

print("Thanks for playing!")
print("We'll see how well you did in next stage")