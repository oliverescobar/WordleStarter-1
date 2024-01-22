# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random


from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():
    def enter_action(s):
        current_row = gw.get_current_row()
        iCount = 0
        next_row = 0 + iCount
        current_word = ""
        for col in range(N_COLS):
            current_word += gw.get_square_letter(current_row, col)
        if current_word in FIVE_LETTER_WORDS:
            gw.show_message('Good job. This is a word.')
            gw.set_current_row(next_row+1)
            iCount = next_row+1
        else:
            gw.show_message("Not in the word list.")
            gw.set_current_row(next_row+1)
            iCount = next_row+1

    gw = WordleGWindow()
    sRandWord=random.choice(FIVE_LETTER_WORDS)
    gw.add_enter_listener(enter_action)
    for iCountRows in range(N_ROWS):
        for iCountColumns in range(N_COLS):
            gw.set_square_letter(iCountRows, iCountColumns, sRandWord[iCountColumns])
            iCountColumns=iCountColumns+1
        iCountRows=iCountRows+1

# Startup code

if __name__ == "__main__":

    wordle()
