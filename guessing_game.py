import random
from statistics import mean, median, mode

scores_list = []


def start_game(scores_list):

    print("Welcome to the number guessing game!")

    tries = 0
    max_number = get_difficulty()

    if len(scores_list) > 0:
        print(f"\nThe current high score is {min(scores_list)}\n")
    else:
        print("\nThere's no high score yet.\n")

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
                singular = "try" if tries == 1 else "tries"
                print(
                    f'Got it! It took you {tries} {singular} to guess the number {random_number}.')
                if len(scores_list) == 0 or tries < min(scores_list):
                    print(
                        f"You set a new high score of {tries} {singular}! 🔥")
                scores_list.append(tries)

                print_scores()
                break

    restart_game()


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


def print_scores():
    print(f"""
Statistics:
You have played {len(scores_list)} {"game" if len(scores_list) == 1 else "games"}.

Your average score is {mean(scores_list):.2f} tries.
Your median score is {median(scores_list)} tries.
Your mode score is {mode(scores_list)} tries.
""")


def restart_game():
    while True:
        restart = input("Do you want to play again? (y/n): ")
        if restart.lower() == "y":
            start_game(scores_list)
            break
        elif restart.lower() == "n":
            print("Thanks for playing!")
            break
        else:
            print("Please enter a valid answer.")
            continue


start_game(scores_list)
