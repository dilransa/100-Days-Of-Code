import random
from Resources import number_guessing

print(number_guessing)

print('Welcome to The Number Guessing Game : ')
print('Computer has selected number between 0-100')

computer =random.randint(0,100)
def compare (limit):
    count = limit

    while count!=0:
        print(f"you have {count} tries")
        user = int(input("Enter your guessing Number : \n"))

        if user == computer:
            print(f'you have won You guess correctly computer guess number is {computer}')
            break

        elif user > computer:
            print('You guessed too High value')

        else:
            print("You guessed too Low Value")

        count -= 1

    if count==0:
        print("You Loose")

ask =input("Do you want to play on Easy mode (E) or Hard mode (H)? : ").lower()

if ask=="e":
    compare(10)

elif ask=='h':
    compare(5)
