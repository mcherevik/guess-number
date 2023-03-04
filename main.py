from random import *


def start_game():
    number = randint(1, 100)
    trials = 0
    print('Welcome to the "Guess the hidden number" game!')
    return number, trials


def is_valid(num):
    if not num.isdigit():
        return False
    if 1 <= int(num) <= 100:
        return True
    else:
        return False


def check_answer():
    while True:
        answer = input()
        if answer.upper() == 'Y':
            return True
        elif answer.upper() == 'N':
            return False
        else:
            print('We do not understand your answer. Please try again')


def compare_numbers(first_num, second_num):
    if first_num > second_num:
        print("Your number is less than the hidden number. Try again")
        return False
    elif first_num < second_num:
        print("Your number is more than the hidden number. Try again")
        return False
    elif first_num == second_num:
        print('Congratulations! You guessed the hidden number')
        return True


number, trials = start_game()
while True:
    print('Please enter a number from 1 to 100')
    user_input = input()
    if not is_valid(user_input):
        print('This is not a valid number. Please try again')
        continue
    elif is_valid(user_input):
        user_number = int(user_input)
    if compare_numbers(number, user_number):
        trials += 1
        print('Your number of trials:', trials)
        print('Do you want to play again? Y / N')
        if check_answer():
            number, trials = start_game()
        else:
            print('Thank you for playing! See you again')
            break
    else:
        trials += 1
