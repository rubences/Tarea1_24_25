from Player import Player
from Opponent import Opponent
from Boss import Boss  

# The score attribute is already defined in the Game class's __init__ method.


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
        if isinstance(self.opponent, Boss) and self.lives > 0:
            print("Congratulations! You defeated the final boss and won the game!")
        else:
            print("Game ended!")
        self.is_running = False

    def reset(self):
        self.score = 0
        self.player = None
        self.opponent = None
        self.is_running = False
        print("Game has been reset.")

    def initialize_player(self, player_name):
        """
        Initializes the player with a given name.
        :param player_name: Name of the player.
        """
        self.player = Player(name=player_name)
        print(f"Player {self.player.name} initialized with {self.player.lives} lives.")
        self.player.initialize_lives()
        self.player.score = 0
        print(f"Player {self.player.name} starts with score {self.player.score}.")
        self.player.lives = 3

    def spawn_player(self, player_name):
        """
        Spawns a player in the game.
        :param
        player_name: Name of the player.
        """
        if self.is_running:
            self.player = Player(name=player_name)
            print(f"Player {self.player.name} spawned!")
        else:
            print("Game is not running. Cannot spawn player.")
        self.player.lives = 3
        print(f"Player {self.player.name} initialized with {self.player.lives} lives.")
        self.player.score = 0
        self.player = Player(name=player_name)
        self.player.lives = 3
        print(f"Player {self.player.name} initialized with {self.player.lives} lives.")


    def update_player(self):
        """
        Updates the player's position and state.
        """
        if self.is_running and self.player:
            print(f"Updating player {self.player.name}...")
            # Add logic to update player's position here
            self.player.move()
            print(f"Player {self.player.name} is moving.")
        else:
            print("Game is not running or no player to update.")
        self.player = Player(name=player_name)
        self.player.lives = 3
        print(f"Player {self.player.name} initialized with {self.player.lives} lives.")
        self.player.score = 0
 

    def spawn_opponent(self, is_star=False):
        """
        Spawns an opponent in the game.
        :param is_star: Boolean indicating if the opponent is a star.
        """
        if self.is_running:
            self.opponent = Opponent(is_star=is_star)
            print(f"Opponent spawned! Is star: {is_star}")
        else:
            print("Game is not running. Cannot spawn opponent.")
        self.opponent = Opponent(is_star=is_star)
        self.opponent.lives = 3
        print(f"Opponent {self.opponent} initialized with {self.opponent.lives} lives.")
        self.opponent.score = 0
        
    def update_opponent(self):
        """
        Updates the opponent's position and state.
        """
        if self.is_running and self.opponent:
            print(f"Updating opponent {self.opponent}...")
            # Add logic to update opponent's position here
            self.opponent.move()
            if self.opponent.is_star:
                print("Opponent is a star!")
            else:
                print("Opponent is not a star.")
        else:
            print("Game is not running or no opponent to update.")
        self.opponent = Opponent(is_star=is_star)
        self.opponent.lives = 3
        print(f"Opponent {self.opponent} initialized with {self.opponent.lives} lives.")
        self.opponent.score = 0
        self.opponent = Opponent(is_star=is_star)

    
    
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

    def initialize_lives(self, lives=3):
        """
        Initializes the player's lives.
        :param lives: Number of lives to start with.
        """
        self.lives = lives
        print(f"Player starts with {self.lives} lives.")

    def lose_life(self):
        """
        Decreases the player's lives by 1. Ends the game if lives reach 0.
        """
        if self.is_running and self.lives > 0:
            self.lives -= 1
            print(f"Player lost a life! Lives remaining: {self.lives}")
            if self.lives == 0:
                print("No lives remaining. Game over!")
                self.end_game()
        else:
            print("Game is not running or no lives left.")

    def spawn_boss(self):
        """
        Spawns a boss when the player defeats an enemy.
        The boss moves twice as fast as a regular opponent.
        """
        if self.is_running:
            self.opponent = Boss(speed_multiplier=2)
            print("A boss has appeared! It moves twice as fast!")
        else:
            print("Game is not running. Cannot spawn a boss.")

    def display_score_and_lives(self):
        """
        Displays the current score and remaining lives of the player.
        """
        if self.is_running:
            print(f"Score: {self.score}, Lives: {self.lives}")
        else:
            print("Game is not running.")
    
    def remove_opponent(self):
        """
        Removes the current opponent and spawns a boss if the opponent is defeated.
        """
        if self.is_running and self.opponent:
            print(f"Opponent {self.opponent} has been defeated!")
            self.opponent = None
            self.spawn_boss()
        else:
            print("Game is not running or no opponent to remove.")