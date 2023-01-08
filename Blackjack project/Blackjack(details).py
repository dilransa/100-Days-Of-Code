import random

def draw_card():

    cards=[2,3,4,5,6,7,8,9,10,"J","Q","K","A"]

    selected_card = random.choice(cards)
    return selected_card


def convert_cards(list):
    for value in list:
        if value=="A":
            index=list.index(value)
            list[index]=11

        elif value in ["K","Q", "J"]:
            index = list.index(value)
            list[index]=10

        else:
            list=list

    return list


def calculation(card):
    if sum(card)==21 and len(card)==2:
        return 21

    if 11 in card:
        if sum(card)>21:
            card.remove(11)
            card.append(1)
    return sum(card)


def compare(user_score, computer_score):
    if (user_score >21  and computer_score>21) or (user_score>21 and computer_score<21):
        return 'You went over you lose'

    if user_score==computer_score:
        return 'It is a Drew'
    elif computer_score==21:
        return 'Lose, opponent has a BlackJack'
    elif user_score==21:
        return 'Win with a Blackjack'
    elif user_score>computer_score:
        return 'You win'
    else:
        return 'you loose'

def play_game():
    user_cards=[]
    computer_cards=[]

    def print_function():
        print(f"You selected : {user_cards} , your score is : {user_sum}")
        print(f"Computer selected : {computer_cards[0]} ")

    play=True

    for i in range(2):
        user_cards.append(draw_card())
        computer_cards.append(draw_card())


    converted_user_cards= convert_cards(user_cards)
    converted_computer_cards = convert_cards(computer_cards)

    user_sum = calculation(converted_user_cards)
    computer_sum = calculation(converted_computer_cards)

    print_function()
    # print(f"You selected : {user_cards} , your score is : {user_sum}")
    # print(f"Computer selected : {computer_cards}[0] ")

    # Ask user to draw another card
    while play:
        ask = input('Do you want to draw another card? Type Y for yes and N for No : ').lower()

        if ask =='y':
            user_cards.append(draw_card())
            converted_user_cards = convert_cards(user_cards)
            user_sum = calculation(converted_user_cards)
            print_function()
        else:
            play=False

    while computer_sum<17:
        computer_cards.append(draw_card())
        converted_computer_cards = convert_cards(computer_cards)
        computer_sum = calculation(converted_computer_cards)

        print(f"You selected : {user_cards} , your score is : {user_sum}")
        print(f"Computer selected : {computer_cards} ,computer score is :{computer_sum} ")

    print(compare(user_score=user_sum,computer_score=computer_sum))


while input("Do you want to play blackJack game ? Type 'y' or 'n' : ")=='y':
    play_game()






