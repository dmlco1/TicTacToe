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