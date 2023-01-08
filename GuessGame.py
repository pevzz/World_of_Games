import random
from Score import add_score
text_open = open('difficulty.txt')
diff = text_open.readline()
difficulty = (int(diff))
max_number = str(5 * difficulty)


def generate_number():
    return int(random.randint(1, (5 * difficulty)))


def get_guess_from_user():
    user_input = input(str("Please enter a number between 1 and " + max_number + ": "))
    try:
        int(user_input)
    except ValueError:
        print("!Wrong value!, please try again")
        print(play())
    return user_input


def compare_results():
    secret_number = int(generate_number())
    guess = int(get_guess_from_user())
    print(guess)
    if guess == secret_number:
        print(True)
        print("Congratulations, You won!")
        add_score()
        again = input("Try again? (y/n)")
        if again == "y":
            print(compare_results())
        elif again == "n":
            print("Until next time")
            import MainGame
            print(MainGame)

    elif guess != secret_number:
        print(False)
        again = input("Try again? (y/n)")
        if again == "y":
            print(compare_results())
        elif again == "n":
            print("Until next time..........")
            import MainGame
            from MainGame import load_game
            print(load_game())

        return ""
    return ""


def play():
    print('''
    
█░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀   ▀█▀ █▀█   ▀█▀ █░█ █▀▀   █▀▀ █░█ █▀▀ █▀ █▀ █ █▄░█ █▀▀   █▀▀ ▄▀█ █▀▄▀█ █▀▀ █
▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄   ░█░ █▄█   ░█░ █▀█ ██▄   █▄█ █▄█ ██▄ ▄█ ▄█ █ █░▀█ █▄█   █▄█ █▀█ █░▀░█ ██▄ ▄
    ''')
    print(compare_results())
    return ""


print(play())

