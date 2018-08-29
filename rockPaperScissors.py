from random import randint

player = input('rock(r) or paper(p) or scissors(s)?')

flag = 0

if(player == 'r' or player == 's' or player == 'p'):
    flag = 1

if(flag != 1):
    while(flag!=1):
        player = input('Wrong input. Try again.')
        if (player == 'r' or player == 's' or player == 'p'):
            flag = 1

print(player, 'vs', end=' ')

chosen = randint(1,3)
#print(chosen)

if(chosen == 1):
    computer = 'r'
elif(chosen == 2):
    computer = 'p'
else:
    computer = 's'

print(computer)

if(player==computer):
    print('Draw')

elif(player=='s' and computer == 'p'):
    print('Player wins.')
elif(player=='s' and computer == 'r'):
    print('Computer wins.')
elif(player=='p' and computer == 'r'):
    print('Player wins.')
elif(player=='p' and computer == 's'):
    print('Computer wins.')
elif(player=='r' and computer == 's'):
    print('Player wins.')
elif(player=='r' and computer == 'p'):
    print('Computer wins.')