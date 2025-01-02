"""
Black Jacket Project

"""
Our Blackjack House Rules
"""
# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

"""
import random
import math

def deal():
    """ Returns random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(list_of_card):
    """ Take a list of cards and returns sum """
    if sum(list_of_card) == 21 and len(list_of_card) == 2:
        return 0
    if 11 in list_of_card and sum(list_of_card) > 21:
        list_of_card.remove(11)
        list_of_card.append(1)
    return sum(list_of_card)

user_card = []
dealer_card = []
end_game = False

for c in range(2):
    user_card.append(deal())
    dealer_card.append(deal())


def compare(user_score, computer_score):
  #Bug fix. If you and the computer are both over, you lose.
    if user_score > 21 and computer_score > 21:
      return "You went over. You lose 😤"
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"
while not end_game:
    user_score = calculate_score(user_card)
    dealer_score = calculate_score(dealer_card)
    print(f"Your cards: {user_card}, current score: {user_score}")
    print(f"Computer's first card: {dealer_card[0]}")

    if user_score == 0 or dealer_score > 21 or user_score == 0:
        end_game = True
    else:
        deal_again = input("Type 'y' to get another card, type 'n' to pass: ")
        if deal_again == 'y':
            user_card.append(deal())
        else:
            end_game = True

while 0 != dealer_score < 17:
    dealer_card.append(deal())
    dealer_score = calculate_score(dealer_card)

print(compare(user_score=user_score,computer_score=dealer_score))
