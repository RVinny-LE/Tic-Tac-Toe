print('Первый игрок - Крестики' + '\n' + 'Второй игрок - Нолики')
Playing_Field = [
                [[' '], [' '], [' ']],
                [[' '], [' '], [' ']],
                [[' '], [' '], [' ']]
                ]
for String in Playing_Field:
    for Item in String:
        print(Item, end = ' ')
    print()


def Check_Winner_Crosses(Playing_Field):
    Flag_C = 0
    if (Playing_Field[0] == [['X'], ['X'], ['X']] or
        Playing_Field[1] == [['X'], ['X'], ['X']] or
        Playing_Field[2] == [['X'], ['X'], ['X']] or
        (Playing_Field[0][0] == Playing_Field[1][0] == Playing_Field[2][0] == ['X']) or
        (Playing_Field[0][1] == Playing_Field[1][1] == Playing_Field[2][1] == ['X']) or
        (Playing_Field[0][2] == Playing_Field[1][2] == Playing_Field[2][2] == ['X']) or
        (Playing_Field[0][0] == Playing_Field[1][1] == Playing_Field[2][2] == ['X']) or
        (Playing_Field[0][2] == Playing_Field[1][1] == Playing_Field[2][0] == ['X'])):
        Flag_C = 1
    return Flag_C


def Check_Winner_Toes(Playing_Field):
    Flag_T = 0
    if (Playing_Field[0] == [['0'], ['0'], ['0']] or
        Playing_Field[1] == [['0'], ['0'], ['0']] or
        Playing_Field[2] == [['0'], ['0'], ['0']] or
        (Playing_Field[0][0] == Playing_Field[1][0] == Playing_Field[2][0] == ['O']) or
        (Playing_Field[0][1] == Playing_Field[1][1] == Playing_Field[2][1] == ['O']) or
        (Playing_Field[0][2] == Playing_Field[1][2] == Playing_Field[2][2] == ['O']) or
        (Playing_Field[0][0] == Playing_Field[1][1] == Playing_Field[2][2] == ['O']) or
        (Playing_Field[0][2] == Playing_Field[1][1] == Playing_Field[2][0] == ['O'])) == 1:
        Flag_T = 1
    return Flag_T


def Check_End_Game(Playing_Field):
    Flag_End = 0
    if (Playing_Field[0][0] == Playing_Field[1][0] == Playing_Field[2][0] != [' '] or 
        Playing_Field[0][1] == Playing_Field[1][1] == Playing_Field[2][1] != [' '] or 
        Playing_Field[0][2] == Playing_Field[1][2] == Playing_Field[2][2] != [' '] or 
        Playing_Field[0][0] == Playing_Field[0][1] == Playing_Field[0][2] != [' '] or 
        Playing_Field[1][0] == Playing_Field[1][1] == Playing_Field[1][2] != [' '] or 
        Playing_Field[2][0] == Playing_Field[2][1] == Playing_Field[2][2] != [' '] or 
        Playing_Field[0][0] == Playing_Field[1][1] == Playing_Field[2][2] != [' '] or 
        Playing_Field[0][2] == Playing_Field[1][1] == Playing_Field[2][0] != [' '] or
        Playing_Field[0].count([' ']) + Playing_Field[1].count([' ']) + Playing_Field[2].count([' ']) == 0):
        Flag_End = 1
    return Flag_End      
count = 0 


while Check_End_Game(Playing_Field) != 1:
    if count % 2 == 0:
        player = 'Первый игрок'
    else:
        player = 'Второй игрок'
    argument = 0
    while argument != 1:
        arg_move = 0 
        while arg_move != 1:
            move_line = input('\n' + f"{player}, введите номер строки," + '\n' +
                              'на которой хотите поставить знак '
                              '(целое число от 1 до 3): \n')
            move_column = input(f"{player}, введите номер столбца," + '\n' +
                                'на котором хотите поставить знак '
                                '(целое число от 1 до 3): \n')
            if (move_line in ['1', '2', '3'] and move_column in
                ['1', '2', '3']):
                arg_move = 1 
                move_line = int(move_line) 
                move_column = int(move_column) 
            else:
                print('Ошибка, введите целое число от 1 до 3 \n')
        if count % 2 == 0:
            if Playing_Field[move_line-1][move_column-1] == [' ']:
                Playing_Field[move_line-1][move_column-1] = ['X']
                argument = 1
                count += 1
            else:
                print('На этой клетке уже стоит знак, поставьте знак '
                      'на пустую клетку \n')
        else:
            if Playing_Field[move_line-1][move_column-1] == [' ']:
                Playing_Field[move_line-1][move_column-1] = ['O']
                argument = 1
                count += 1 
            else:
                print('На этой клетке уже стоит знак, поставьте знак '
                      'на пустую клетку \n')
    for String in Playing_Field:
        for Item in String:
            print(Item, end = ' ')
        print()


if Check_Winner_Crosses(Playing_Field):
    print('Победил первый игрок')
elif Check_Winner_Toes(Playing_Field):
    print('Победил второй игрок')
else:
    print('Ничья')


input("Нажмите Enter для выхода!")