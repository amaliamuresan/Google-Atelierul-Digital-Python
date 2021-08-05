from tkinter import *
import tkinter

window = Tk()
window.geometry('330x370')
window.title('TicTacToe')
window.resizable(False, False)

score_zero = 0
score_one = 0

color_zero = '#368F8B'
color_one = '#FFDF5D'

score_frame = Frame(window, width=100, height=50, bd=0)
score_frame.pack(side=TOP)

score_text = StringVar()
score_text.set('Score: {0} - {1}'.format(score_zero, score_one))

score_label = tkinter.Label(score_frame, textvariable=score_text, height=2)
score_label.grid(row=0, column=0, padx=1, pady=1)

button_reset = Button(score_frame, text='Play Again', fg='black', width=8, height=1, bd=0, bg='green', cursor='hand2')
button_reset.grid(row=0, column=1, padx=1, pady=1)

winner_text = StringVar()
winner_text.set('')
winner_label = tkinter.Label(score_frame, textvariable=winner_text, height=2)
winner_label.grid(row=1, column=0, padx=1, columnspan=2, pady=1)

btns_frame = Frame(window, width=300, height=300, bg='grey')
btns_frame.pack()

sq_table = []


class MyButton:
    def __init__(self, button, row, col):
        self.button = button
        self.button.configure(command=self.btn_click)

        self.row = row
        self.col = col

    def btn_click(self):
        global table, player, color_one, color_zero
        if type(self.button) == Button and table[self.row][self.col] == -1 and player != -1:
            if player == 0:
                self.button.configure(bg=color_zero)
                player = 1
                table[self.row][self.col] = 0
            else:
                self.button.configure(bg=color_one)
                player = 0
                table[self.row][self.col] = 1
            check_game_state()

    def reset_button(self):
        self.button.configure(bg='black')
        table[self.row][self.col] = -1


def check_game_state():
    global table, score_zero, score_one, score_label, player
    potential_winner = check_if_winner(table)
    print(potential_winner)
    if potential_winner != -1:
        if potential_winner == 0:
            score_zero += 1
            winner_text.set('Blue Player wins!')
        else:
            score_one += 1
            winner_text.set('Yellow Player wins!')
        player = -1
    else:
        if verify_valid_positions_exists(table) == -1:
            winner_text.set('Draw!')

    score_text.set('Score: {0} - {1}'.format(score_zero, score_one))


def is_winner_on_row(mat):
    for row in mat:
        if row.count(1) == 3:
            return 1
        elif row.count(0) == 3:
            return 0
    return -1


def is_winner_on_column(mat):
    for i in range(3):
        col = [row[i] for row in mat]
        if col.count(1) == 3:
            return 1
        if col.count(0) == 3:
            return 0
    return -1


def is_winner_on_diagonals(mat):
    diagonal = [mat[i][i] for i in range(3)]
    if diagonal.count(0) == 3:
        return 0
    if diagonal.count(1) == 3:
        return 1
    diagonal = [mat[i][2-i] for i in range(3)]
    if diagonal.count(0) == 3:
        return 0
    if diagonal.count(1) == 3:
        return 1
    return -1


def check_if_winner(mat):
    if is_winner_on_diagonals(mat) != -1:
        return is_winner_on_diagonals(mat)
    elif is_winner_on_column(mat) != -1:
        return is_winner_on_column(mat)
    elif is_winner_on_row(mat) != -1:
        return is_winner_on_row(mat)
    return -1


def verify_valid_positions_exists(mat):
    for i in mat:
        if i.count(-1):
            return 0
    return -1


def draw_table():
    global sq_table
    for i in range(0, 3):
        # table_line = []
        for j in range(0, 3):
            sq = Button(btns_frame, text='', fg='black', width=15, height=6, bd=0, bg='black', cursor='hand2')
            sq.grid(row=i, column=j, padx=1, pady=1)
            myButton = MyButton(sq, i, j)
            sq_table.append(myButton)
            # table_line.append(myButton)
        # sq_table.append(table_line)


def play_game():
    draw_table()


def reset_game():
    global player, sq_table
    player = 0
    winner_text.set('')
    for button in sq_table:
        if type(button) is MyButton:
            button.reset_button()


button_reset.configure(command=reset_game)
play_game()
print(sq_table)
table = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
player = 0
window.mainloop()
