
# Rock paper Scessor
# Conditions
# R>S
# S>P
# P>R


import random


while True:
    user_input = input('What do you choose? Type R for rock, P for paper , S for scissor ?').lower()
    computer_choice=random.choice(['R','P','S']).lower()
    print(f'Computer choice is {computer_choice}')

    if user_input not in ['r','p','s']:
        print('Invalid input')
        continue

    if user_input== computer_choice:
        print('it\'s a tie')

    elif (user_input=='r' and computer_choice=='s') or (user_input=='s'and computer_choice=='p') or (user_input=='p'and computer_choice=='r'):
        print('Congratulations you have won')
    else:
        print("you've lost")






