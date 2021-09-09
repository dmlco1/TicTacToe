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

X.draw_x(X(1, screen))
C.draw_c(C(9, screen))


def see_x():
    pass

# draw board lines
Line.draw_lines(Line(screen))

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


# end game after win and announce the winner
def end_game():
    print("{} is the winner!!".format(winner))
    sys.exit()


# turn of the current player
def turn():
    turn_time = True

    while turn_time:
        print("\nYour move {}!".format(current_player))
        position = int(input("Insert a number from 1-9: "))
        # check if input is valid or not
        if position < 0 or position > 9:
            print("Invalid input, try again")
        # check if the position chosen is already occupied
        elif board[position - 1] != "-":
            print("Position already occupied, try again")
        # if OK then the turn is ended
        else:
            turn_time = False

    # set position
    board[position - 1] = current_player
    display_board()


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


# check if there is a win
def check_win():
    global winner

    # see if theres is a win
    if (check_rows() or check_columns()) or check_diagonals():
        end_game()


# check if there is a tie
def check_tie():
    if "-" not in board:
        end_game_with_tie()


# check if the game has ended
def check_game_ended():
    check_win()
    if game_continues:
        check_tie()


# change player after end of turn
def change_player():
    global current_player  # define as global variable so we can access it
    # if player is X change to O
    if current_player == "X":
        current_player = "O"
    # if player is O change to X
    else:
        current_player = "X"


# game engine
def play_game():
    # display board
    display_board()

    while game_continues:
        turn()
        # check if the game is over
        check_game_ended()
        # change player
        change_player()
    end_game()


# update screen
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

play_game()