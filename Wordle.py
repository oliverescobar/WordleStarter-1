# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random


from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():
    gw = WordleGWindow()
    sRandWord=random.choice(FIVE_LETTER_WORDS)
    for iCountRows in range(N_ROWS):
        for iCountColumns in range(N_COLS):
            gw.set_square_letter(iCountRows, iCountColumns, sRandWord[iCountColumns])
            iCountColumns=iCountColumns+1
        iCountRows=iCountRows+1


    def enter_action(s):
        gw.show_message("You have to implement this method.")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# Startup code

if __name__ == "__main__":
    wordle()
