from Entity import Entity

class Character(Entity):
    def __init__(self, lives):
        super().__init__()
        self.lives = lives
        self.is_alive = lives > 0

    def move(self, direction):
        """
        Moves the character in the specified direction.
        :param direction: A string indicating the direction (e.g., 'up', 'down', 'left', 'right').
        """
        # Implement movement logic here
        pass

    def shoot(self):
        """
        Allows the character to shoot.
        """
        # Implement shooting logic here
        pass

    def collide(self, other_entity):
        """
        Handles collision with another entity.
        :param other_entity: The entity this character collides with.
        """
        # Implement collision logic here
        pass