import random

def number_guessing_game():
    randNum = random.randint(0, 10)
    
    print('Welcome to Number Guessing Game!')
    
    while True:
        try:
            guess = int(input("Enter your guess (0-10): "))
            if guess < 0 or guess > 10:
                print("Please enter a number within the range 0-10.")
                continue
            
            if guess > randNum:
                print("Try Again Lower.")
            elif guess < randNum:
                print("Try Again Higher.")
            else:
                print("Congratulations! You guessed the correct number.")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

number_guessing_game()