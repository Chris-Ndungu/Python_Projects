import random

# Create the options for the game - rock, paper, scissors and quit
options = ['rock', 'paper', 'scissors']

computer_scores = 0
user_scores =0

# The user picks an aption to play against the computer
# Check the winner by going through the win/loss options

while True:
    user_pick = input("Select Rock/Paper/Scissors to play or q to quit: ").strip().lower()

    # Computer randomnly selects an option to play with
    random_number = random.randint(0, 2)

    computer_pick = options[random_number]

    # quit
    if (user_pick == "q"):
        break

    # check if user has won
    if (user_pick not in options):
        continue

    # check if user has won
    if (user_pick == computer_pick):
        print("It's a Tie!")
    elif(user_pick == 'rock' and computer_pick == 'scissors'):
        print("You won!")
        user_scores += 1
    elif (user_pick == 'paper' and computer_pick == 'rock'):
        print("You won!")
        user_scores += 1
    elif (user_pick == 'scissors' and computer_pick == 'paper'):
        print("You won!")
        user_scores += 1
    else:
        print("You lost!")
        computer_scores += 1

# Output the scores for both the player and the computer
print("\nPlayer wins:", str(user_scores) + ".")
print("Computer wins:", str(computer_scores) + ".")

print("Goodbye!")