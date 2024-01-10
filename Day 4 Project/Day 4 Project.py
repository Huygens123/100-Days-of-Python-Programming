import random
"""
Challenge day 4

"""

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
choice_list = [rock, paper, scissors]
choice_num = len(choice_list)
# player choice
player_choice = int(input("What do you choose? Type 0 for Rock, 21 for Paper or 2 for Scissors. \n"))
if player_choice == 0:
    print("You chose \n" + rock)
elif player_choice == 1:
    print("You chose \n" + paper)
else:
    print("You chose \n" + scissors)

# computer choice

computer_choice = random.randint(0, choice_num -1)
if computer_choice == 0:
    print("Computer chose \n" + rock)
elif computer_choice == 1:
    print("Computer chose \n" + paper)
else:
    print("Computer chose \n" + scissors)

# decision

if computer_choice == 0 and player_choice == 2:         # decision 1
    print("You Lose!")
elif computer_choice == 2 and player_choice == 1:         # decision 2
    print("You Lose!")
elif computer_choice == 1 and player_choice == 0:         # decision 3
    print("You Lose!")
else:
    print("You won!")
