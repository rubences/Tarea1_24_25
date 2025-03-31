class Game:
    def __init__(self):
        self.score = 0
        self.player = None
        self.opponent = None
        self.is_running = False

    def start(self):
        self.is_running = True
        self.score = 0
        print("Game started!")

    def update(self):
        if self.is_running:
            print("Game is updating...")
            # Add logic to update game state here
        else:
            print("Game is not running.")

    def end_game(self):
        self.is_running = False
        print("Game ended!")

    def reset(self):
        self.score = 0
        self.player = None
        self.opponent = None
        self.is_running = False
        print("Game has been reset.")

    def serialize(self):
        """
        Serializes the game state.
        :return: A dictionary representing the game state.
        """
        return {
            "score": self.score,
            "is_running": self.is_running,
            "player": self.player.serialize() if self.player else None,
            "opponent": self.opponent.serialize() if self.opponent else None
        }
    def deserialize(self, data):
        """"
        Deserializes the game state from a dictionary."
        """
        self.score = data["score"]
        self.is_running = data["is_running"]
        if data["player"]:
            self.player = Player()
            self.player.deserialize(data["player"])
        if data["opponent"]:
            self.opponent = Opponent()
            self.opponent.deserialize(data["opponent"])

    def __str__(self):
        """
        Returns a string representation of the game.
        :return: A string representing the game state.
        """
        return f"Game state: score={self.score}, running={self.is_running}, player={self.player}, opponent={self.opponent}"
    
    def convert_enemy_to_star(self, enemy):
        """
        Converts an enemy to a star and increments the score.
        :param enemy: The enemy to be converted.
        """
        if self.is_running and enemy:
            print(f"Enemy {enemy} converted to a star!")
            self.score += 1
        else:
            print("Game is not running or invalid enemy.")
    