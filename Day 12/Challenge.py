import  random
def guess_no():
    random_number = []
    for i in range(1,100):
        random_number = random.choice(i)
        return random_number

difficulty = input('Choose a difficulty. "easy" or "hard":')
easy = 10
hard = 5
make_guess = int(input('Make a guess: '))
guess = guess_no
start = True

while start:
    if difficulty == 'easy':
        print(f'You have {easy} attempts remaing to guess the number')
        if guess > make_guess:
            print('Too low')
            print(f'You have{easy} attempts remaining')
            print("Guess again")
            easy -= 1
        elif guess < make_guess:
            print('Too high')
            print(f'You have{easy} attempts remaining')
            print("Guess again")
            easy -= 1
        else:
            print('Correct!')
            start = False

    else:
        print(f'You have {hard} attempts remaing to guess the number')
        if guess > make_guess:
            print('Too low')
            print(f'You have{hard} attempts remaining')
            print("Guess again")
            hard -= 1
        elif guess < make_guess:
            print('Too high')
            print(f'You have{hard} attempts remaining')
            print("Guess again")
            hard -= 1
        else:
            print('Correct!')
            start = False



