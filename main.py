# Создайте программу для игры в "Крестики-нолики"

import emoji
from isOdd import isOdd


# Инициализация
x = emoji.emojize(":cross_mark:")
o = emoji.emojize(":hollow_red_circle:")
board = [i for i in range(1, 10)]
win_lines= [[0,1,2],
            [3,4,5],
            [6,7,8],
            [0,3,6],
            [1,4,7],
            [2,5,8],
            [0,4,8],
            [2,4,6]]


# Отрисовка игровой доски
def draw_board(board):
    _ = [print(board[0 + i * 3], board[1 + i * 3], board[2 + i * 3]) for i in range(3)]


# Проверка игрового поля
def check_win(board):
    for line in win_lines:
        if board[line[0]] == x and board[line[1]] == x and board[line[2]] == x:
            return x
        elif board[line[0]] == o and board[line[1]] == o and board[line[2]] == o:
            return o


# Сделать ход
def step_game(symbol):
    while True:
        try:
            pos = int(input(f"Введите позицию '{symbol}': "))
        except ValueError:
            continue
        if pos >= 1 and pos <= 9:
            if str(board[pos - 1]).isdigit():
                board[pos - 1] = symbol
                break


# tic-tac-toe
count = 0
while True:
    draw_board(board)
    if not isOdd(count):
        step_game(x)
    else:
        step_game(o)
    count += 1
    smb = check_win(board)
    if smb:
        print(f"Выиграл '{smb}'!")
        break
    if count == 9:
        print("Ничья!")
        break