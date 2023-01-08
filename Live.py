name = input('Enter Your Name: ')


def write_gamechoice(x):
    choice = open('gamechoice.txt', mode='w')
    choice.write(x)
    choice.close()


def write_difficulty(y):
    diff_choice = open('difficulty.txt', mode='w')
    diff_choice.write(y)
    diff_choice.close()


def welcome():
    print("Hello " + name + "! and welcome to the World of Games (WoG).Here you can find many cool games to play.")
    return " "


def load_game():
    print('''
Please choose a game to play:

1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
2. Guess Game - guess a number and see if you chose like the computer
3. Currency Roulette - try and guess the value of a random amount of USD in ILS
    ''')

    def game_choices():
        game_choice = (input('Enter your choice: '))
        if game_choice == str("1"):
            print("Loading game...")
            write_gamechoice("1")
        elif game_choice == str("2"):
            print("Loading game...")
            write_gamechoice("2")
        elif game_choice == str("3"):
            print("Loading game...")
            write_gamechoice("3")
        else:
            print('Invalid choice')
            print(load_game())
            return " "
        return ""

    def game_difficulty():
        difficulty = (input('Please choose game difficulty from 1 to 5: '))
        if difficulty == str("1"):
            print("difficulty set to 1")
            write_difficulty("1")
        elif difficulty == str("2"):
            print("difficulty set to 2")
            write_difficulty("2")
        elif difficulty == str("3"):
            print("difficulty set to 3")
            write_difficulty("3")
        elif difficulty == str("4"):
            print("difficulty set to 4")
            write_difficulty("4")
        elif difficulty == str("5"):
            print("difficulty set to 5")
            write_difficulty("5")
        else:
            print('Invalid choice')
            print(game_difficulty())
            return ""
        return ""

    def game_import():

        text_open = open('gamechoice.txt')
        choice = text_open.readline()
        game_choice = (int(choice))
        if game_choice == 1:
            import MemoryGame
            print(MemoryGame)
        elif game_choice == 2:
            import GuessGame
            print(GuessGame)
        elif game_choice == 3:
            import CurrencyRouletteGame
            print(CurrencyRouletteGame)
        else:
            print("")

    print(game_choices())
    print(game_difficulty())
    print(".")
    print("..")
    print("...")
    print(game_import())
    return ""
