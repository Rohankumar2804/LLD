

if __name__ == '__main__':
    from ChessGame.enums import Color
    from ChessGame.game_manager import GameManager
    from ChessGame.models.player import Player
    player1 = Player("Alice", Color.WHITE)
    player2 = Player("Bob", Color.BLACK)

    game = GameManager(player1, player2)
    game.play()