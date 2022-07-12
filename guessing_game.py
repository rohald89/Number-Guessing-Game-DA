import random


def start_game(high_score=100):

    print(f"""
Welcome to the number guessing game!
You have to guess a number between 1 and 100.
The current high score is {high_score}.
""")

    tries = 0
    answer = random.randint(1, 100)
    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
        except ValueError:
            print("Please enter a number.")
            continue
        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            continue
        else:
            tries += 1
            if guess > answer:
                print("It's lower.")
                continue
            elif guess < answer:
                print("It's higher.")
                continue
            else:
                print(f"You got it! It took you {tries} tries.")
                if tries < high_score:
                    high_score = tries
                    print(f"You set a new high score of {high_score} tries!")
                break

    restart_game(high_score)


def restart_game(high_score):
    while True:
        restart = input("Do you want to play again? (y/n): ")
        if restart.lower() == "y":
            start_game(high_score)
        elif restart.lower() == "n":
            print("Thanks for playing!")
            break
        else:
            print("Please enter a valid answer.")
            continue


start_game()
