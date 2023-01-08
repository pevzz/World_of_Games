import os
from time import sleep



def SCORES_FILE_NAME():
    score = open('Scores.txt')
    return print(score.readline())

def BAD_RETURN_CODE():
    print("Error 404 ,please try again")
    return ""

def Screen_cleaner():
    print("The screen will be cleaned up in a few seconds...")
    sleep(4)
    os.system('cls')
    return ""

