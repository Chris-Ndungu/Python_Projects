import random
import os
from art import logo

print("Welcome to BlackJack Game!!\n")

def deal_card():
    ''' Returns a random card from the deck '''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    return random.choice(cards)

# Claculate scores
def calculate_scores(cards):
    ''' Takes a list of cards and returns their sum '''

    # Check for  Blackjack
    blackjack = [11, 10]
    
    if (all(value in cards for value in blackjack) and len(cards) == 2):
        return 0
    
    # check for ace
    ace = 11
    if (ace in cards and sum(cards) > 21 and len(cards) < 3):
        cards.remove(ace)
        cards.append(1)

    return (sum(cards))

# compare user's and computer's results
def compare_results (user_score, computer_score):
    if (user_score == computer_score):
        return "Draw 🙃"
    elif (computer_score == 0):
        return "Lose, Opponent has BlackJack 😞"
    elif (user_score == 0):
        return "Win with a BlackJack 😎"
    elif (user_score > 21) :
        return "You went over. You lose 🥹"
    elif (computer_score > 21):
        return "Opponent went over. You win 🫡"
    elif (user_score > computer_score):
        return "You win 😃"
    else:
        return "You lose 😥"

# function for playing the game
def play_game():

    print(logo)
    
    #deal the user and the computer with 2 cards each
    user_cards = []
    computer_cards =[]
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())


    while not is_game_over:
        user_score = calculate_scores(user_cards)
        computer_score = calculate_scores(computer_cards)

        '''  '''
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer first card: {computer_cards[0]}")


        # check if the game has ended
        if (user_score == 0 or computer_score == 0 or user_score > 21):
            is_game_over = True
        else:
            another_draw = input("Do you want to draw another card? (y/n) ").strip().lower()

            if another_draw == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # computer deals after the user has finished as long as the score is less than 17
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_scores(computer_cards)

    # show the results
    print(compare_results(user_score, computer_score))

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

# ask if user wants to play the game
while input("Do you want to play the game of Blackjack? Type 'y' or 'n': ") == 'y':
    #clear the screen
    os.system('clear')
    play_game()
