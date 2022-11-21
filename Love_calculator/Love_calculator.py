
print('Welcome to the LOVE calculator')

person_1 = input('Enter Your name? ').lower()
person_2 =  input('Enter your name? ').lower()

name= person_1+person_2

T= name.count('t')
R= name.count('r')
U= name.count('u')
E= name.count('e')

TRUE =T+R+U+E
value_1=0

if TRUE > 10:
    for i in str(TRUE):
        value_1+= int(i)

else:
    value_1 = T + R + U + E

L= name.count('r')
O= name.count('r')
V= name.count('r')

LOVE =L+O+V+E
value_2=0

if LOVE > 10:
    for i in str(LOVE):
        value_2+= int(i)

else:
    value_2 = L+O+V+E


value=str(value_1)+str(value_2)


print(f'Your love value is {value}%')