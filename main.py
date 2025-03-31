from Game import Game

if __name__ == "__main__":
    game = Game()
    game.start()
    game.spawn_player("Player1")
    game.spawn_opponent(is_star=True)
    game.update_opponent()
    game.update_player()
    game.player.shoot()
    game.opponent.shoot()
    game.update()
    game.end_game()
    game.reset()