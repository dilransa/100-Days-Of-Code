print('welcome to the Tip Calculator')

a=int(input('What was the total bill ? '))
b=int(input('How many people to split the bill? '))
c= int(input('What is the  percentage of the tip you would like to give? '))

price= a*(1+(c/100))

amount_erson= round(price/b)

print(f'there are {b} number of people to devide the bill and price of the bill is {a} and tip is {c}% so each person would pay {amount_erson}')