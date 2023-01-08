import random
from Score import add_score
from currency_converter import CurrencyConverter
text_open = open('difficulty.txt')
diff = text_open.readline()
difficulty = (int(diff))
print(''' 
░█████╗░██╗░░░██╗██████╗░██████╗░███████╗███╗░░██╗░█████╗░██╗░░░██╗
██╔══██╗██║░░░██║██╔══██╗██╔══██╗██╔════╝████╗░██║██╔══██╗╚██╗░██╔╝
██║░░╚═╝██║░░░██║██████╔╝██████╔╝█████╗░░██╔██╗██║██║░░╚═╝░╚████╔╝░
██║░░██╗██║░░░██║██╔══██╗██╔══██╗██╔══╝░░██║╚████║██║░░██╗░░╚██╔╝░░
╚█████╔╝╚██████╔╝██║░░██║██║░░██║███████╗██║░╚███║╚█████╔╝░░░██║░░░
░╚════╝░░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝░╚════╝░░░░╚═╝░░░

██████╗░░█████╗░██╗░░░██╗██╗░░░░░███████╗████████╗████████╗███████╗
██╔══██╗██╔══██╗██║░░░██║██║░░░░░██╔════╝╚══██╔══╝╚══██╔══╝██╔════╝
██████╔╝██║░░██║██║░░░██║██║░░░░░█████╗░░░░░██║░░░░░░██║░░░█████╗░░
██╔══██╗██║░░██║██║░░░██║██║░░░░░██╔══╝░░░░░██║░░░░░░██║░░░██╔══╝░░
██║░░██║╚█████╔╝╚██████╔╝███████╗███████╗░░░██║░░░░░░██║░░░███████╗
╚═╝░░╚═╝░╚════╝░░╚═════╝░╚══════╝╚══════╝░░░╚═╝░░░░░░╚═╝░░░╚══════╝  ''')

def get_money_interval():
    global interval
    c = CurrencyConverter()
    # print(c.convert(1, 'USD', 'ILS'))
    t = random.randint(1, 100)
    print("USD: " + str(t) + "$")
    interval = range(t-(5-difficulty),t+(5-difficulty))
    return interval


def get_guess_from_user():
    global guess
    c = CurrencyConverter()
    crncy = c.convert(1, 'USD', 'ILS')
    user_guess = int(input("Please enter the value of the number above in ILS: "))
    guess = round(user_guess / crncy)
    return guess

def play():
    get_money_interval()
    get_guess_from_user()
    if guess in interval:
        print(True)
        add_score()
    else:
        print(False)
    choice = input("Would you like to play again? (y/n): ")
    if choice == "y":
        print(play())
    else:
        from MainGame import load_game
        print(load_game())



play()