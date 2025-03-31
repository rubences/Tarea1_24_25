from Character import Character

class Player(Character):
    def __init__(self, name, score=0, lives=3):
        super().__init__(name)
        self.score = score
        self.lives = lives

    def move(self, direction):
        # Implement movement logic here
        print(f"{self.name} moves {direction}")

    def shoot(self):
        # Implement shooting logic here
        print(f"{self.name} shoots!")

    def collide(self, other_entity):
        # Implement collision logic here
        print(f"{self.name} collides with {other_entity.name}")

    def reset(self):
        # Reset player-specific attributes
        self.score = 0
        self.lives = 3
        print(f"{self.name} has been reset.")
    
    def serialize(self):
        """
        Serializes the player's state.
        :return: A dictionary representing the player's state.
        """
        data = super().serialize()
        data.update({
            "score": self.score,
            "lives": self.lives
        })
        return data
    def deserialize(self, data):
        """"
        "Deserializes the player's state from a dictionary."
        """
        super().deserialize(data)
        self.score = data["score"]
        self.lives = data["lives"]
    def __str__(self):
        return f"Player {self.name} with score {self.score} and lives {self.lives}"
    
    