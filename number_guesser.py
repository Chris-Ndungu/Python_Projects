import random

# Get the top of the range number
top_of_range = input("Enter the top of the range number: ")

# Check whether the input is a number
if (top_of_range.isdigit()):
    top_of_range = int(top_of_range)

    if (top_of_range == 0):
        print("Please enter a number greater than zero next time")
        quit()

else:
    print("Please enter a number next time")
    quit()

# Create a loop for the user to guess a number until they win

computer_number = random.randint(0, top_of_range)
# create a score for the number of guesses
guesses = 0

while True:
    # User guess
    guesses += 1
    user_guess = input("Make a guess: ")

    if (user_guess.isdigit()):
        user_guess = int(user_guess)
    else:
        print("Please enter a number")
        continue

    if (user_guess == computer_number):
        print("You got it! :)")
        break
    elif (user_guess > computer_number):
        print("Your guess is above the number!")
    elif (user_guess < computer_number):
        print("Your guess is below the number!")

# Output the number of guesses
print("You got it in", guesses, "guesses!!!")