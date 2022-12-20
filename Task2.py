# Создайте программу для игры в ""Крестики-нолики""

print ('Начало игры КРЕСТИКИ-НОЛИКИ. Игроки ходят по очереди, первый игрок использует Х, второй - O')


board = ['1','2','3','4','5','6','7','8','9']

def Grid(array):
    for i in range (0,8,3):
        print (array[i], array[i+1], array[i+2])
    return ''

for i in range (1,len(board)+1): 
    if i % 2 == 0:
        sequence = "Ход ВТОРОГО игрока (o)"
    else:
        sequence = "Ход ПЕРВОГО игрока (x)"
    print (sequence, 'Введите через пробел номер поля и символ, например 5 x')
    print(Grid(board))
    x = 'x'
    o = 'o'
    turn = input().split(' ')
    board[int(turn[0])-1] = turn[1]
            
    if x in board[0] and x in board[1] and x in board[2]:
        print('Игра окончена. Выиграл игрок Х')
        break
    elif x in board[3] and x in board[4] and x in board[5]:
        print('Игра окончена. Выиграл игрок Х')
        break
    elif x in board[6] and x in board[7] and x in board[8]:
        print('Игра окончена. Выиграл игрок Х')
        break
    elif x in board[0] and x in board[3] and x in board[6]:
        print('Игра окончена. Выиграл игрок Х')
        break    
    elif x in board[1] and x in board[4] and x in board[7]:
        print('Игра окончена. Выиграл игрок Х')
        break
    elif x in board[2] and x in board[5] and x in board[8]:
        print('Игра окончена. Выиграл игрок Х')
        break
    elif x in board[0] and x in board[4] and x in board[8]:
        print('Игра окончена. Выиграл игрок Х')
        break
    elif x in board[2] and x in board[4] and x in board[6]:
        print('Игра окончена. Выиграл игрок Х')
        break
    elif o in board[0] and o in board[1] and o in board[2]:
        print('Игра окончена. Выиграл игрок O')
        break
    elif o in board[3] and o in board[4] and o in board[5]:
        print('Игра окончена. Выиграл игрок O')
        break
    elif o in board[6] and o in board[7] and o in board[8]:
        print('Игра окончена. Выиграл игрок O')
        break
    elif o in board[0] and o in board[3] and o in board[6]:
        print('Игра окончена. Выиграл игрок O')
        break    
    elif o in board[1] and o in board[4] and o in board[7]:
        print('Игра окончена. Выиграл игрок O')
        break
    elif o in board[2] and o in board[5] and o in board[8]:
        print('Игра окончена. Выиграл игрок O')
        break
    elif o in board[0] and o in board[4] and o in board[8]:
        print('Игра окончена. Выиграл игрок O')
        break
    elif o in board[2] and o in board[4] and o in board[6]:
        print('Игра окончена. Выиграл игрок O')
        break
    elif i == 9:
        print ('Игра окончена. Ничья')


