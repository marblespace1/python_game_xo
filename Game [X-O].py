# from curses.ascii import isdigit
def greet():
    print(' --------------- ')
    print(' Крестики-нолики ')
    print('     ver 1.0     ')
    print(' --------------- ')
    print('    2022 year    ')
    print(' VVVVVVVVVVVVVVV ')

greet()

field = [[" "] * 3 for i in range (3)]
# field

def show():
    print(f'  | 0 | 1 | 2 |')
    print (' -------------- ')
    for i in range (3):
        row_info = " | ".join(field[i])
        print (f'{i} | {row_info} | ')
        print(' -------------- ')

row = field[0]
# show()

def check_win():
    win_cord = [((0,0), (0,1), (0,2)), ((1,0), (1,1), (1,2)), ((2,0), (2,1), (2,2)),
                  ((0,2), (1,1), (2,0)), ((0,0), (1,1), (2,2)), ((0,0), (1,0), (2,0)),
                  ((0,1), (1,1), (2,1)), ((0,2), (1,2), (2,2))]
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            show()
            print ("Выиграл X!")
            return True
        if symbols == ["0", "0", "0"]:
            show()
            print("Выиграл 0!")
            return True
    return False

check_win()

def ask():
    while True:
        coords = input('     Введите координаты по х и y через пробел:  ').split()

        if len(coords) != 2:
            print(' Введите 2 координаты! ')
            continue

        x, y = coords
        # x, y = int(x), int(y)

        if not (x.isdigit()) or not (y.isdigit()):
            print(" Введите только числа!")
        else:
            x, y = int(x), int(y)

            if 0 > x or x > 2 or 0 > y or y > 2 :
                print (" Координаты вне диапазона! ")
                continue

            if field[x][y] != " ":
                print(" Клетка занята! ")
                continue

            return x, y

# ask()

num = 0
while True:
    num += 1

    show()

    if num % 2 ==1:
        print(" Ходит крестик ")
    else:
        print(" Ходит нолик ")

    x, y = ask()

    if num % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if check_win():
        break

    if num == 9:
        print (" Ничья! ")
        break











