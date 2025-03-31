from Entity import Entity
from Shot import Shot  # Import the Shot class

class Character(Entity):
    def __init__(self, lives):
        super().__init__()
        self.lives = lives


    def move(self, direction):
        """
        Moves the character in the specified direction.
        :param direction: A string indicating the direction (e.g., 'up', 'down', 'left', 'right').
        """
        if direction == 'up':
            self.y -= 1
        elif direction == 'down':
            self.y += 1
        elif direction == 'left':
            self.x -= 1
        elif direction == 'right':
            self.x += 1
        else:
            raise ValueError("Invalid direction. Use 'up', 'down', 'left', or 'right'.")

    def shoot(self):
        """
        Allows the character to shoot.
        """
        # Create a new shot instance at the character's current position
        shot = Shot(self.x, self.y, direction="up")  # Assuming shots move 'up' by default

        # Return the shot instance so it can be added to the game world or handled further
        return shot

    def collide(self, other_entity):
        """
        Handles collision with another entity.
        :param other_entity: The entity this character collides with.
        """
        if self.is_alive and other_entity.is_alive:
            # Example logic: reduce lives if the other entity is an enemy
            if hasattr(other_entity, "is_enemy") and other_entity.is_enemy:
                self.lives -= 1
                if self.lives <= 0:
                    self.is_alive = False
                    print("Game Over! The character has no lives left.")
                    # Logic to end the game can be added here

            # Additional logic for colliding with the boss
            if hasattr(other_entity, "is_boss") and other_entity.is_boss:
                self.lives = 0
                self.is_alive = False
                print("Game Over! The boss defeated the character.")
                # Logic to handle boss collision and end the game can be added here

    def reset(self):
        """
        Resets the character's state.
        """
        self.lives = 3
        self.is_alive = True
        # Reset other character-specific attributes here
        pass

    def __str__(self):
        """
        Returns a string representation of the character.
        :return: A string representing the character's state.
        """
        return f"Character with {self.lives} lives, alive: {self.is_alive}, position: ({self.x}, {self.y}), image: {self.image}"

