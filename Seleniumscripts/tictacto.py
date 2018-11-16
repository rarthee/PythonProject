i=0

tup1=()
inparr = list('123456789')
inparrnew=['1','2','3','4','5','6','7','8','9']
print('\n'.join(' '.join(inparr[x:x+3]) for x in(0,3,6)))
# positions(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)
result=''
i=0


while (i<9):
    if (i%2==0):
        p=int(input("Enter player 1 position"))
        if(inparrnew[p - 1] == ('X' or 'O')):
            p = int(input("Position already entered. Enter a new position"))
        inparrnew[p-1]='X'
        print('\n'.join(' '.join(inparrnew[x:x + 3]) for x in (0, 3, 6)))
    else:
        p=int(input("Enter player 2 position"))
        if (inparrnew[p - 1] == ('X' or 'O')):
            p = int(input("Position already entered. Enter a new position"))
        inparrnew[p-1]='O'
        print('\n'.join(' '.join(inparrnew[x:x + 3]) for x in (0, 3, 6)))

    if inparrnew[0]=='X' and  inparrnew[1] =='X' and  inparrnew[2] =='X':
        print("The winner is Player 1")
        exit()
    elif  (inparrnew[3]=='X' and  inparrnew[4] =='X' and  inparrnew[5] =='X'):
        print("The winner is Player 1")
        exit()
    elif (inparrnew[6] == 'X' and inparrnew[7] == 'X' and inparrnew[8] == 'X'):
        print("The winner is Player 1")
        exit()
    elif (inparrnew[0] == 'X' and inparrnew[3] == 'X' and inparrnew[6] == 'X'):
        print("The winner is Player 1")
        exit()

    elif (inparrnew[2] == 'X' and inparrnew[5] == 'X' and inparrnew[8] == 'X'):
        print("The winner is Player 1")
        exit()
    elif (inparrnew[0] == 'X' and inparrnew[4] == 'X' and inparrnew[8] == 'X'):
        print("The winner is Player 1")
        exit()
    elif (inparrnew[2] == 'X' and inparrnew[4] == 'X' and inparrnew[6] == 'X'):
        print("The winner is Player 1")
        exit()
    ##check for player2
    if inparrnew[0]=='O' and  inparrnew[1] =='O' and  inparrnew[2] =='O':
        print("The winner is Player 1")
        exit()
    elif  (inparrnew[3]=='O' and  inparrnew[4] =='O' and  inparrnew[5] =='O'):
        print("The winner is Player 1")
        exit()
    elif (inparrnew[6] == 'O' and inparrnew[7] == 'O' and inparrnew[8] == 'O'):
        print("The winner is Player 1")
        exit()
    elif (inparrnew[0] == 'O' and inparrnew[3] == 'O' and inparrnew[6] == 'O'):
        print("The winner is Player 1")
        exit()

    elif (inparrnew[2] == 'O' and inparrnew[5] == 'O' and inparrnew[8] == 'O'):
        print("The winner is Player 1")
        exit()
    elif (inparrnew[0] == 'O' and inparrnew[4] == 'O' and inparrnew[8] == 'O'):
        print("The winner is Player 1")
        exit()
    elif (inparrnew[2] == 'O' and inparrnew[4] == 'O' and inparrnew[6] == 'O'):
        print("The winner is Player 1")
        exit()
    i = i + 1