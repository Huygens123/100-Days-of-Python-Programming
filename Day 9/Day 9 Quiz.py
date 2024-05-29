import os

bid = {}
bidding_finished = False

def auction(bidding_record):

    highest_bid = 0
    highest_bidder = ""

    for bidder in bidding_record:
        amount_bid = bidding_record[bidder]
        if amount_bid > highest_bid:
            highest_bid = amount_bid
            highest_bidder = bidder
    print(f"The highest bidder is {highest_bidder} with bid ${highest_bid}")


while not bidding_finished:
    auction_name = input("Please enter your name name: \n")
    amount_bid = int(input("How much do you want to bid? \n"))
    bid[auction_name] = amount_bid
    should_continue = input("Are there any other bidder? 'no' or 'yes'? ").lower()
    if should_continue == 'no':
        bidding_finished = True
        auction(bidding_record=bid)
    elif should_continue == 'yes':
        os.system('cls')




#auction(name=amount_bid, amount=amount_bid, direction=dire)


