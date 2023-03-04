from random import *


def start_game():
    print('Welcome to the "Guess the hidden number" game!')
    while True:
        print('Please enter the upper border')
        border = input()
        if is_valid(border):
            hidden_number = randint(1, int(border))
            init_trials = 0
            return hidden_number, init_trials, int(border)
        else:
            print('This is not a valid number. Try again')
            continue


def is_valid(num):
    if num.isdigit() and 1 <= int(num):
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


number, trials, upper_border = start_game()
while True:
    print('Please enter a number from 1 to', upper_border)
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
            number, trials, upper_border = start_game()
        else:
            print('Thank you for playing! See you again')
            break
    else:
        trials += 1
