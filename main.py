import random

# CLASSES
class Player():
    def __init__(self, which_player = None, score = 0):
        self.score = score
        self.which_player = which_player
        self.current_choice = None


    def increase_score(self):
        self.score += 1
    
    def player_chooses(self):
        self.current_choice = input(f"Player {self.which_player}, please select a box (IE: 'b2'): \nInput: ").strip().lower()
        print(f"you chose: {self.current_choice}")
        return self.current_choice
    
    def __str__(self) -> str:
        return f"Player {self.which_player}, score: {self.score}, current choice: {self.current_choice}"

class Board():
    def __init__(self) -> None:
        self.options = {
            'a1': '', 'b1': '', 'c1': '',
            'a2': '', 'b2': '', 'c2': '',
            'a3': '', 'b3': '', 'c3': '',
            }
        
    def mark_board(self, player):
        self.options[player.current_choice] = player.which_player
        self.update()
    
    def update(self):
        print(self)
    
    def __str__(self):
        return f"""
           A  B  C
        1) {self.options['a1']} | {self.options['b1']} | {self.options['c1']}
           ----------
        2) {self.options['a2']} | {self.options['b2']} | {self.options['c2']}
           ----------
        3) {self.options['a3']} | {self.options['b3']} | {self.options['c3']}
        """

def init_game():
    global options, board, turn, Player
    turn_counter = 1
    game_is_on = True

    # WELCOME MESSAGE
    def welcome():
        print('''
        --------------------------
          Let's play Py-Pac-Poe!
        --------------------------
        ''')
    
    x_player = Player('X')
    o_player = Player('O')
    board = Board()


        # self.options = {
        #     'a1': ' ', 'b1': ' ', 'c1': ' ',
        #     'a2': ' ', 'b2': ' ', 'c2': ' ',
        #     'a3': ' ', 'b3': ' ', 'c3': ' ',
        #     }
    def win_check(board):
        global game_is_on
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

    
    welcome()
    board.update()
    while game_is_on:
        if turn_counter % 2 != 0:
            take_turn(x_player, board)
        else: 
            take_turn(o_player, board)
        turn_counter += 1
        if turn_counter > 9 or win_check(board): 
            break

init_game()