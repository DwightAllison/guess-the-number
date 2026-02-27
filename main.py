import random

def choose_difficulty() -> tuple[int, int]:
    """
    Ask the user to choose a difficulty and return (min_num, max_num).
    Easy = 1-10, Normal = 1-20, Hard = 1-100
    """
    while True:
        print("\nChoose difficulty:")
        print("1) Easy (1-10)")
        print("2) Normal (1-20)")
        print("3) Hard (1-100)")

        choice = input("Enter 1, 2, or 3: ").strip()

        if choice == "1":
            return (1, 10)
        elif choice == "2":
            return (1, 20)
        elif choice == "3":
            return (1, 100)
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def get_guess(min_num: int, max_num: int) -> int:
    """Prompt the user until they enter a valid whole number within range."""
    while True:
        user_input = input(f"Guess a number from {min_num}-{max_num}: ").strip()

        if user_input.isdigit():
            guess = int(user_input)
            if min_num <= guess <= max_num:
                return guess

        print(f"Please enter a whole number from {min_num} to {max_num}.")

def play_one_game(min_num: int, max_num: int) -> None:
    print(f"\nGuess the number game ({min_num}-{max_num})")
    secret = random.randint(min_num, max_num)
    attempts = 0

    while True:
        guess = get_guess(min_num, max_num)
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
        min_num, max_num = choose_difficulty()
        play_one_game(min_num, max_num)

        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play()