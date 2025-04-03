import random

def number_guessing_game():
    print("I'm thinking of a number between 1 and 100.")
    
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    print(f"You have {max_attempts} attempts to guess the number.")
    
    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts!")
                return
                
            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"You have {remaining} attempts remaining.")
            else:
                print("This was your last attempt.")
                
        except ValueError:
            print("Please enter a valid number between 1 and 100.")
    
    print(f"\nGame over! The number was {secret_number}.")
    print("Better luck next time!")

if __name__ == "__main__":
    number_guessing_game()
    play_again = input("Would you like to play again? (yes/no): ").lower()
    while play_again == 'yes':
        number_guessing_game()
        play_again = input("Would you like to play again? (yes/no): ").lower()
    print("Thanks for playing! Goodbye.")