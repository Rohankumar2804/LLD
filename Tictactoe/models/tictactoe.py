from typing import List

from Tictactoe.models.board import Board


class TicTacToe:
    board : Board
    players : List
    turn : int
    def __init__(self,size,player1,player2):
        self.board = Board(size)
        self.players = [player1,player2]
        self.turn = 0

    def switch_turn(self):
        self.turn = 1-self.turn

    def play(self):
        print("🎮 Welcome to Tic Tac Toe!")
        self.board.display()

        while True:
            player = self.players[self.turn]
            print(f"{player.name}'s turn ({player.symbol})")

            try:
                row, col = map(int, input("Enter row and column (0-based index): ").split())
            except ValueError:
                print("Invalid input. Enter two numbers separated by space.")
                continue

            if not (0 <= row < self.board.size and 0 <= col < self.board.size):
                print("Invalid cell. Try again.")
                continue

            if not self.board.is_empty(row, col):
                print("Cell already taken. Try again.")
                continue

            self.board.update_cell(row, col, player.get_symbol())
            self.board.display()

            if self.board.is_winner(player.get_symbol().get_value()):
                print(f"🎉 {player.name} wins!")
                break

            if self.board.is_full():
                print("It's a draw!")
                break

            self.switch_turn()

