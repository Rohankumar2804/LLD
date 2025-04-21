from Tictactoe.models.player import Player
from Tictactoe.models.symbol import Symbol
from Tictactoe.models.tictactoe import TicTacToe

if __name__ == "__main__":
    x_symbol = Symbol("X")
    o_symbol = Symbol("O")

    p1 = Player("Player 1", x_symbol)
    p2 = Player("Player 2", o_symbol)

    try:
        board_size = int(input("Enter board size (e.g. 3 for 3x3): "))
    except ValueError:
        print("Invalid size, defaulting to 3.")
        board_size = 3

    game = TicTacToe(board_size,p1, p2)
    game.play()
