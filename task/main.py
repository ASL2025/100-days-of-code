#TODO: Ace can be 1 or 11. 1 if total goes over then 21 and 11 if total less then 21
#TODO: at first only 1 card is shown by the computer and two for player
#TODO: if my total is less than 17 and its my turn then chose hit or stand
#TODO: if in their turn they get more than 17 they have to stop and compare
#TODO: always start with my turn
#TODO: show what is in your hand and what is in computer's hand
#TODO: take cards till sum not more than 17
#TODO 1: show selected cards of player and their sum and also one card from computer
import random
import os
player_cards = []
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# two random cards

length_no_1 = 0
while length_no_1 < 2:
    one_card = random.choice(cards)
    player_cards.append(one_card)
    length_no_1 += 1
# your_final_hand =
# computers_final_hand =

current_score = 0
number_of_cards = len(player_cards)
for i in range(number_of_cards):
    current_score += player_cards[i]


print(f"Your cards: {player_cards}, current_score: {current_score}")

# deal two cards to computer
computer_card = []
length = 0
while length <2:
    pc_card = random.choice(cards)
    computer_card.append(pc_card)
    length += 1

pcs_card = f"Computer's chosen cards: {computer_card}"
print(pcs_card)

#sum of computer's cards
computer_score = 0
number_of_card = len(computer_card)
for i in range(number_of_card):
    computer_score += computer_card[i]
print(f"Computer's score: {computer_score}")

# TODO: now type y to get another card , type n to pass

option_value = input("now type y to get another card , type n to pass").lower()
if option_value == 'y':
    another_card = random.choice(cards)
    player_cards.append(another_card)
    print(player_cards)

# if its a blackjack
if (computer_score == 21) or (current_score == 21):
    if computer_score == 21:
        print("PC has a blackjack..you lose!!")
    else:
        print("you have a blackjack..you win!!")
elif (computer_score > 21) or (current_score > 21):
    if current_score > 21:
        for card in player_cards:
            if card == 11:
                current_score += 1 - card
                if current_score > 21:
                    print("You lose!")
                else:
                    option_value = input("now type y to get another card , type n to pass").lower()
                    if option_value == y:
                        another_card2 = player_cards.append(cards)
                        print(player_cards)

            else:
                print("You lose!")
print("Current Working Directory:", os.getcwd())