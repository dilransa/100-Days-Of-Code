import random
# Importing Data dictionary and try to select one randomly
from Resources import data
# Select a responses
def response():
    list_index = random.randint(0, 49)
    return data[list_index]


def search_index(dict):
    dict.index('dict')

answer = ''
play = True
count = 0
index = 0
B = response()

while play:
    if count > 0:
        A = B
        B = response()

    else:
        A = response()
        B = response()
    while B == A:
        B = response()

    print(f"Compare A : {A['name']}, {A['description']}, from {A['country']} ")
    #print(A['follower_count'])
    print(f"Compare B : {B['name']}, {B['description']}, from {B['country']} ")
    #print(B['follower_count'])


    def select_max(A, B):
        if A['follower_count'] > B['follower_count']:
            return 'A'
            maximizer = A
        elif A['follower_count'] < B['follower_count']:
            return 'B'
            maximizer = B
        else:
            return 'EQUAL'

    max = select_max(A, B)

    ask = input("Who has more followers Type 'A' or 'B': ").upper()

    if max == ask:
        count += 1
        print(f"You're right! Current score:{count}")
    else:
        print(f"Sorry, that's wrong. Final score: {count}")
        play = False
