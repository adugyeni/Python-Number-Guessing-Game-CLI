import random 

def guess_number():
    target = random.randint(1, 100)
    attempt_counter = 0
    max_attempts = 5

    print("Heyya 👋, Let's play a game..." \
    "I'm thinking of a number between 1 and 100. Guess it!")

    while attempt_counter <= max_attempts:
        try:
            guess = int(input("Your guess: "))
            attempt_counter += 1

            if guess < target:
                print("Too low! Try again.")
            elif guess > target:
                print("Too high! Try again.")
            else:
                print(f"Hurray!!! You guessed it right in {attempt_counter} attempts.")
                return
        except ValueError:
            print("Invalid input. Please enter a number")

    print(f"Game Over❌ The correct number is {target}. Better luck next time.")

guess_number()