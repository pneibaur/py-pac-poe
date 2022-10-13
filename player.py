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