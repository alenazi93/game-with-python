import random

options = ['rock', 'paper', 'scissors']

while True:
# Get user input
user_choice = input("Enter rock, paper, or scissors (or 'q' to quit): ")
user_choice = user_choice.lower()

# Check if the user wants to quit
if user_choice == 'q':
break

# Check if the user's input is valid
if user_choice not in options:
print("Invalid input. Please enter rock, paper, or scissors.")
continue

# Generate the computer's choice
computer_choice = random.choice(options)

# Determine the winner
if user_choice == computer_choice:
print("Tie!")
elif user_choice == 'rock' and computer_choice == 'scissors':
print("You win!")
elif user_choice == 'paper' and computer_choice == 'rock':
print("You win!")
elif user_choice == 'scissors' and computer_choice == 'paper':
print("You win!")
else:
print("Computer wins!")
