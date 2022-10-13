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