import random
from Score import add_score
import time
text_open = open('difficulty.txt')
diff = text_open.readline()
difficulty = (int(diff))
list_a = [0]
list_b = [0]

print('''
╭╮╭╮╭╮╱╱╭╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭╮╱╱╱╱╱╭╮╭╮╱╱╱╱╱╭━╮╭━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━━━╮╱╱╱╱╱╱╱╱╭╮
┃┃┃┃┃┃╱╱┃┃╱╱╱╱╱╱╱╱╱╱╱╱╱╭╯╰╮╱╱╱╭╯╰┫┃╱╱╱╱╱┃┃╰╯┃┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃╭━╮┃╱╱╱╱╱╱╱╱┃┃
┃┃┃┃┃┣━━┫┃╭━━┳━━┳╮╭┳━━╮╰╮╭╋━━╮╰╮╭┫╰━┳━━╮┃╭╮╭╮┣━━┳╮╭┳━━┳━┳╮╱╭╮┃┃╱╰╋━━┳╮╭┳━━┫┃
┃╰╯╰╯┃┃━┫┃┃╭━┫╭╮┃╰╯┃┃━┫╱┃┃┃╭╮┃╱┃┃┃╭╮┃┃━┫┃┃┃┃┃┃┃━┫╰╯┃╭╮┃╭┫┃╱┃┃┃┃╭━┫╭╮┃╰╯┃┃━╋╯
╰╮╭╮╭┫┃━┫╰┫╰━┫╰╯┃┃┃┃┃━┫╱┃╰┫╰╯┃╱┃╰┫┃┃┃┃━┫┃┃┃┃┃┃┃━┫┃┃┃╰╯┃┃┃╰━╯┃┃╰┻━┃╭╮┃┃┃┃┃━╋╮
╱╰╯╰╯╰━━┻━┻━━┻━━┻┻┻┻━━╯╱╰━┻━━╯╱╰━┻╯╰┻━━╯╰╯╰╯╰┻━━┻┻┻┻━━┻╯╰━╮╭╯╰━━━┻╯╰┻┻┻┻━━┻╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯ ''')

def generate_sequence():
    rnd_number = random.sample(range(102), difficulty)
    print(rnd_number, end="\r")
    time.sleep(3)
    print(" " * len(rnd_number), end="\r")
    time.sleep(1)
    print("                    ")
    global list_a
    list_a = list_a + rnd_number
    return " "


def get_list_from_user():
    user_input = input("Enter the numbers you remember, separated by space: ")
    try:
        int(user_input)
    except ValueError:
        print("!Wrong value!, please try again")
        print(play())
    list_split = user_input.split()
    list_input = list(map(int, list_split))
    print(list_input)
    global list_b
    list_b = list_b + list_input
    return ""


def is_list_equal():
    if list_a == list_b:
        print(True)
        add_score()
        return ""
    else:
        print(False)


def play():
    generate_sequence()
    get_list_from_user()
    is_list_equal()
    choice = input("Would you like to play again? (y/n): ")
    if choice == "y":
        print(play())
    else:
        from MainGame import load_game
        print(load_game())


play()




