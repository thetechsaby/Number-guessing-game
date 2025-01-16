# import random
# def number_guessing_game():
#   print("Welcome to the number guessing game")
#   target_number = random.randint(1,100)
#   attempts = 0

#   try:
#     while True:
#       user_guess = int(input("Guess a number between (1-100)"))
#     attempts += 1
#     if user_guess == target_number:
#       print (f"Congratulations! you guessed the correct number {target_number} in {attempts} attempts." )
#       break
#     elif user_guess < target_number:
#       print ("too low, try again")
#     else:
#       print("too high, try again")

#   except ValueError:
#       print("Error: enter a valid number.")

# number_guessing_game()



# import random

# def number_guessing_game():
#     print("Welcome to the number guessing game")
#     target_number = random.randint(1, 100)
#     attempts = 0

#     try:
#         while True:
#             user_guess = int(input("Guess a number between (1-100): "))
#             attempts += 1
#             if user_guess == target_number:
#                 print(f"Congratulations! You guessed the correct number {target_number} in {attempts} attempts.")
#                 break
#             elif user_guess < target_number:
#                 print("Too low, try again")
#             else:
#                 print("Too high, try again")
#     except ValueError:
#         print("Error: Please enter a valid number.")

# # Start the game
# number_guessing_game()

import random

def number_guessing_game():
    print("welcome to the number guessing game")
    target_number = random.randint(1, 100)
    attempts = 0

    try:
        while true:
            user_guess = int(input("Enter a number between (1-100): "))
            attempts += 1
            if user_guess == target_number:
                print (f" congratulations! you have guessed the correct number {target_number} in {attempts} attempts")
                break
            elif user_guess < target_number:
                print ("too low, try again")
            else:
                print("too high, try again")
    except ValueError:
        print("Error: please enter a valid number")

    number_guessing_game()







