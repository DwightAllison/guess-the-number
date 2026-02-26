import random

MIN_NUM = 1
MAX_NUM = 20

def get_guess() -> int:
    """Prompt the user until they enter a valid whole number within range."""
    while True:
        user_input = input(f"Guess a number from {MIN_NUM}-{MAX_NUM}: ").strip()

        if user_input.isdigit():
            guess = int(user_input)
            if MIN_NUM <= guess <= MAX_NUM:
                return guess

        print(f"Please enter a whole number from {MIN_NUM} to {MAX_NUM}.")

def play_one_game() -> None:
    print("\nGuess the number game")
    secret = random.randint(MIN_NUM, MAX_NUM)
    attempts = 0

    while True:
        guess = get_guess()
        attempts += 1

        if guess == secret:
            print(f"Correct! You got it in {attempts} tries.")
            break
        elif guess < secret:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")

def play() -> None:
    while True:
        play_one_game()
        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play()