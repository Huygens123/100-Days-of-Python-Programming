This project implements a text-based Blackjack game with these key components:

Game Rules:
Unlimited deck, no jokers
Face cards = 10, Ace = 1 or 11
Computer acts as dealer

Core Functions:

deal(): Returns random card from deck
calculate_score(): Sums cards, handles Ace values
compare(): Determines winner based on scores

Game Flow:

Deals initial 2 cards to player and dealer
Player can hit ('y') or stand ('n')
Dealer must hit on 16 and below
Checks for Blackjack and bust conditions
