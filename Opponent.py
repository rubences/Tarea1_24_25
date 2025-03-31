from Character import Character
from Shot import Shot  # Import the Shot class

class Opponent(Character):
    def __init__(self, is_star=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_star = is_star

    def __str__(self):
        return f"Opponent with {self.lives} lives and is_star={self.is_star}"

    def move(self):
        """
        Implements the logic for the opponent's movement.
        Opponents move horizontally back and forth across the screen.
        """
        if self.position.x <= 0 or self.position.x >= self.screen_width - self.width:
            self.velocity.x = -self.velocity.x  # Reverse direction when hitting screen edges
        self.position.x += self.velocity.x

    def shoot(self):
        """
        Implements the logic for the opponent's shooting.
        Creates a Shot instance and sets its initial position and velocity.
        """
        if self.is_alive:
            # Create a new shot originating from the opponent's position
            shot = Shot(
                position=self.position.copy(),  # Start at the opponent's position
                velocity=self.velocity.copy(),  # Use the opponent's velocity as a base
                owner=self,  # Set the owner of the shot to this opponent
                type="opponent_bullet"  # Specify the type of the shot
            )
            # Adjust the shot's velocity to move downward (towards the player)
            shot.velocity.y = abs(shot.velocity.y)  # Ensure it moves downward
            return shot
        return None

    def collide(self, other_entity):
        """
        Handles collision with another entity.
        :param other_entity: The entity this opponent collides with.
        """
        if other_entity.type == "player_bullet":
            self.is_alive = False
            other_entity.owner.score += 1  # Increment the player's score
        pass
    def reset(self):
        """"
        "Resets the opponent's state.
        """
        self.lives = 3
        self.is_alive = True
        # Reset other opponent-specific attributes here
        pass
 

    