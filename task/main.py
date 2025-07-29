#TODO: Ace can be 1 or 11. 1 if total goes over then 21 and 11 if total less then 21
#TODO: at first only 1 card is shown by the computer and two for player
#TODO: if my total is less than 17 and its my turn then chose hit or stand
#TODO: if in their turn they get more than 17 they have to stop and compare
#TODO: always start with my turn
#TODO: show what is in your hand and what is in computer's hand
#TODO: take cards till sum not more than 17
#TODO 1: show selected cards of player and their sum and also one card from computer
import random
import art

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def compare(u_score, c_score):
    """Compares the user score u_score against the computer score c_score."""
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"

#always try to make small functions out of the concepts
# use remove() to delete by value, not by index.
def calculate_score(list_of_cards):
    if sum(list_of_cards) == 21 and len(list_of_cards) == 2:
        return 0
    if sum(list_of_cards) > 21 and 11 in list_of_cards:
        list_of_cards.append(1)
        list_of_cards.remove(11)
    score = sum(list_of_cards)
    return score

def play_game():
    print(art.logo)
    user_cards = []
    user_score = -1
    computer_score = -1
    computer_cards = []

    game_over = False
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if computer_score == 0 or user_score == 0 or user_score > 21:
            game_over = True
        else:
            one_more_card = input("Type y if you want to draw another card or type n to pass: ")
            if one_more_card == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True

    if computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, your final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, computer's final score: {computer_score}")
    print(compare(user_score,computer_score))

while input("Do you want to play the game blackjack again. type 'y' or 'n'..") == 'y':
    print('\n' * 20)
    play_game()
    print("yoyo")