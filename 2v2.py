import sys
import pygame
from Lines import X, C, Line

pygame.init()

WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# If game is still going
game_continues = True

# current player
current_player = "X"
screen.fill((102, 153, 204))
# winner
winner = None

# draw board lines
Line.draw_lines(Line(screen))
# update screen
pygame.display.flip()

# create board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]


def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


# end game with a tie
def end_game_with_tie():
    print("It´s a Tie!!\n Congratulations to both X and O")
    sys.exit()


# check if player completed a row
def check_rows():
    global game_continues
    global winner

    # see the logical values of the following conditions
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"

    # if one of them is True then there's a winner and we stop the game
    if row1 or row2 or row3:
        winner = current_player
        game_continues = False
        print("\nWinner!!!")


# check if player completed a column
def check_columns():
    global game_continues
    global winner

    # see the logical values of the following conditions
    column1 = board[0] == board[3] == board[6] != "-"
    column2 = board[1] == board[4] == board[7] != "-"
    column3 = board[2] == board[5] == board[8] != "-"

    # if one of them is True then there's a winner and we stop the game
    if column1 or column2 or column3:
        winner = current_player
        game_continues = False
        print("\nWinner!!!")


# check if player completed a diagonal
def check_diagonals():
    global game_continues
    global winner

    # see the logical values of the following conditions
    diagonal1 = board[0] == board[4] == board[8] != "-"
    diagonal2 = board[2] == board[4] == board[6] != "-"

    # if one of them is True then there's a winner and we stop the game
    if diagonal1 or diagonal2:
        winner = current_player
        game_continues = False
        print("\nWinner!!!")


# check if there is a win
def check_win():
    global winner

    # see if theres is a win
    if (check_rows() or check_columns()) or check_diagonals():
        print("\nWWWWWinner!!!")
        sys.exit()
    else:
        pass


# check if there is a tie
def check_tie():
    if "-" not in board:
        end_game_with_tie()
    else:
        pass


# check if the game has ended
def check_game_ended():
    check_win()
    if game_continues:
        check_tie()
    else:
        sys.exit()


def find_position(row_chosen, col_chosen):
    pos_number = 0

    if row_chosen == 0:
        if col_chosen == 0:
            pos_number = 1
        elif col_chosen == 1:
            pos_number = 2
        elif col_chosen == 2:
            pos_number = 3
    if row_chosen == 1:
        if col == 0:
            pos_number = 4
        elif col == 1:
            pos_number = 5
        elif col == 2:
            pos_number = 6
    if row_chosen == 2:
        if col_chosen == 0:
            pos_number = 7
        elif col_chosen == 1:
            pos_number = 8
        elif col_chosen == 2:
            pos_number = 9

    return pos_number


def turn(row_chosen, col_chosen):
    global current_player
    turn_time = True

    while turn_time:
        # check if the position chosen is already occupied
        if board[find_position(row_chosen, col_chosen) - 1] != "-":
            pass
        # if OK then the turn is ended
        else:
            turn_time = False

    # set position
    board[find_position(row_chosen, col_chosen) - 1] = current_player
    display_board()


def draw_player(row_chosen, col_chosen):
    global current_player
    if current_player == "X":
        turn(row_chosen, col_chosen)
        X.draw_x(X(find_position(row_chosen, col_chosen), screen))
    else:
        turn(row_chosen, col_chosen)
        C.draw_c(C(find_position(row_chosen, col_chosen), screen))


# change player after end of turn
def change_player():
    global current_player  # define as global variable so we can access it
    # if player is X change to O
    if current_player == "X":
        current_player = "O"
    # if player is O change to X
    else:
        current_player = "X"


for event in pygame.event.get():

    event_happened = False
    while not event_happened:
        event = pygame.event.wait()

        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            coord_x = event.pos[0]
            coord_y = event.pos[1]

            # divide the coordinates by 200 gives us numbers between 0 and 2 equivalent to number os rows and
            # columns
            row = int(coord_y // 200)
            col = int(coord_x // 200)

            draw_player(row, col)
            # game_continues = False
            # check if the game is over
            check_game_ended()
            # change player
            change_player()
            event_happened = True
            pygame.display.update()
