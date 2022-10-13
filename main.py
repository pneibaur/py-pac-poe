from player import Player
from board import Board

def init_game():

    # INSTANTIATE CLASSES
    x_player = Player('X')
    o_player = Player('O')
    board = Board()

    # WELCOME MESSAGE
    def welcome():
        print('''
        --------------------------
          Let's play Py-Pac-Poe!
        --------------------------
        ''')
        board.update()

    def win_check(board):
        option = board.options
        print("win checking...")
        if option['a1'] == option['a2'] and option['a1'] == option['a3']:
            print(f"we have a winner!")
            return True
        else:
            print("no win yet! ")
            return False
    
    def take_turn(player, board):
        taking_turn = True
        while taking_turn:
            player.player_chooses()
            if player.current_choice == None or player.current_choice not in board.options.keys():
                print("You must type a valid choice.")
                continue
            elif board.options[player.current_choice]:
                print("That spot is already taken. Try again!")
                continue
            else:
                board.mark_board(player)
                player.current_choice = None
                break

    def game_play():
        game_is_on = True
        turn_counter = 1
        while game_is_on:
            print("turn counter: ", turn_counter)
            if turn_counter % 2 != 0:
                take_turn(x_player, board)
            else: 
                take_turn(o_player, board)
            turn_counter += 1
            if turn_counter > 9 or win_check(board): 
                break

    welcome()
    game_play()

init_game()