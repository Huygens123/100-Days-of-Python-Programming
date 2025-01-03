from game_data import data
from Art import logo, vs
import random

def format_data(account):
    account_name = account['name']
    account_dec = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_dec}, from {account_country}"

def get_answer(guesses, a_follow, b_follow):
    """
    Get guess from user and check if they are right or not
    """
    if a_follow > b_follow:
        return guesses == 'a'
    else:
        return guesses == 'b'

print(logo)

score = 0

should_continue = True
account_b = random.choice(data)

while should_continue:
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    guess = input("Who has more followers? 'A' or 'B': ").lower()

    a_follower_account = account_a['follower_count']
    b_follower_account = account_b['follower_count']

    is_correct = get_answer(guess, a_follower_account, b_follower_account)

    if is_correct:
        score += 1
        print(f"You're right, your score is {score}")
    else:
        should_continue = False
        print(f"Sorry, that's wrong. Your score is {score}")