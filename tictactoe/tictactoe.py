# 5 stage

EMPTY = ' '
X = 'X'
O = 'O'

WIN = 'win'
DRAW = 'draw'
IN_PROGRESS = 'in progress'

field = [[EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY]]


def fieldf():                                                                         #вывод поля
    print('---------')
    for i in field:
        print('|', ' '.join(i), '|')
    print('---------')


def user_input():                                                                     #ввод пользователя и его проверка
    while True:
        try:
            i, s = map(int, input("Enter the coordinates: ").split())

            if not (1 <= i <= 3 and 1 <= s <= 3):
                print("Coordinates should be from 1 to 3!")

            elif field[i - 1][s - 1] != EMPTY:
                print("This cell is occupied! Choose another one!")

            else:
                return (i - 1, s - 1)

        except ValueError:
            print("You should enter numbers!")


def check_field():                                                                      #проверить поле
    for i in range(3):
    # строки
        if field[i] == [X, X, X]:
            return WIN
        if field[i] == [O, O, O]:
            return WIN

    # колонки
        if field[0][i] == X and field[1][i] == X and field[2][i] == X:
            return WIN
        if field[0][i] == O and field[1][i] == O and field[2][i] == O:
            return WIN

    # диагонали
    if field[0][0] == X and field[1][1] == X and field[2][2] == X:
        return WIN
    if field[0][2] == X and field[1][1] == X and field[2][0] == X:
        return WIN
    if field[0][0] == O and field[1][1] == O and field[2][2] == O:
        return WIN
    if field[0][2] == O and field[1][1] == O and field[2][0] == O:
        return WIN

    # ничья
    for i in field:
        for cell in i:
            if cell == EMPTY:
                return IN_PROGRESS
    return DRAW

def game():
    state = IN_PROGRESS
    current_player = X

    fieldf()

    while state == IN_PROGRESS:
        i, col = user_input()
        field[i][col] = current_player
        state = check_field()
        fieldf()
        if state == IN_PROGRESS:
            current_player = O if current_player == X else X

    if state == WIN:
        print(f"{current_player} win")
    else:
        print("Draw")

game()


