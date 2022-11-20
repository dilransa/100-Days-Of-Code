
import random
##Generating a random word
#words= ["apple",'banana','kaggle','stereo']
from Resources import word_list
chosen_word = random.choice(word_list)
end_of_game= False
lives=6

from Resources import logo
print(logo)

#testing
#print(f'chosen word is {chosen_word}')

#Generating as many as blanks as the letters included(adding to a list)
L=[]
for _ in chosen_word:
    L.append("_")



# Ask user to guess a letter

while not end_of_game:
    guess= input('WHat is your guess letter ? \n')

    if guess in L:
        print(f'you\'ve used {guess} already')

    for index in range(len(chosen_word)):
        if chosen_word[index]==guess:
            L[index]=guess

    if guess not in chosen_word:
        print(f'{guess} letter not in the word ')
        lives-=1
        if lives==0:
            print('You\'ve lost')
            end_of_game=True

    #Convert list into a string

    answer=''
    for i in L:
        answer+=i

    print(answer)

    ##attaching ascii
    from Resources import stages
    if guess not in chosen_word:
        print(stages[lives])




    if "_" not in L:
        print('Congradulations you have won')
        end_of_game=True







