import random
from statistics import mean, median, mode


def start_game(high_score=None, scores_list=[]):

    print("Welcome to the number guessing game!")

    tries = 0
    max_number = get_difficulty()

    print(f"""
You have to guess a number between 1 and {max_number}.
The current high score is {high_score or max_number}.
""")

    random_number = random.randint(1, max_number)

    while True:
        try:
            guess = int(input(f"Guess a number between 1 and {max_number}: "))
        except ValueError:
            print("Please enter a number.")
            continue
        if guess < 1 or guess > max_number:
            print(f"Please enter a number between 1 and {max_number}.")
            continue
        else:
            tries += 1
            if guess > random_number:
                print("It's lower.")
                continue
            elif guess < random_number:
                print("It's higher.")
                continue
            else:
                print(f"\nYou got it! It took you {tries} tries.")
                if high_score == None or tries < high_score:
                    high_score = tries
                    print(f"You set a new high score of {high_score} tries!")

                scores_list.append(tries)
                print_scores(scores_list)
                break

    restart_game(high_score)


def restart_game(high_score):
    while True:
        restart = input("Do you want to play again? (y/n): ")
        if restart.lower() == "y":
            start_game(high_score)
            break
        elif restart.lower() == "n":
            print("Thanks for playing!")
            break
        else:
            print("Please enter a valid answer.")
            continue


def print_scores(scores_list):
    print(f"""
Data:
Mean: {mean(scores_list)}
Median: {median(scores_list)}
Mode: {mode(scores_list)}
""")


def get_difficulty():
    max_number = 100

    difficulty = int(input("""
Please choose a difficulty level:
1. Easy (1-10)
2. Medium (1-100)
3. Hard (1-1000)
> """))
    if difficulty == 1:
        max_number = 10
    elif difficulty == 2:
        max_number = 100
    elif difficulty == 3:
        max_number = 1000
    elif difficulty == 4:
        print("You asked for it... 🤷")
        max_number = 10000
    else:
        print("Please enter a valid difficulty level.")
        get_difficulty()
    return max_number


start_game()
