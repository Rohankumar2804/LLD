from ChessGame.models.board import Board
from ChessGame.models.move import Move
from ChessGame.models.player import Player


class GameManager:
    def __init__(self, player1: Player, player2: Player):
        self.board = Board()
        self.players = [player1, player2]
        self.current_turn = 1  # 0 or 1
        self.moves = []
    def get_current_player(self):
        return self.players[self.current_turn]

    def switch_turn(self):
        self.current_turn = 1 - self.current_turn

    def is_game_over(self):
        # Checkmate/stalemate detection can be improved
        kings = [cell.piece for row in self.board.grid for cell in row if cell.piece and cell.piece.symbol == "K"]
        return len(kings) < 2

    def play(self):
        while not self.is_game_over():
            player = self.get_current_player()
            print(f"{player.name} ({player.color})'s turn")
            self.board.print_board()

            from_x = int(input("From row: "))
            from_y = int(input("From col: "))
            to_x = int(input("To row: "))
            to_y = int(input("To col: "))

            source = self.board.get_cell(from_x, from_y)
            dest = self.board.get_cell(to_x, to_y)
            print(source.piece.color)
            if source.piece is None:
                print("Invalid move. No piece at source.")
                continue
            print(player.color)
            print(source.piece.color!=player.color)
            if source.piece.color != player.color:
                print("Invalid move. Not your piece.")
                continue

            if not source.piece.can_move(source, dest,self.board):
                print("Invalid move. Piece can't move there.")
                continue

            # Move
            move = Move(source, dest,source, dest)
            self.moves.append(move)

            dest.piece = source.piece
            source.piece = None

            self.switch_turn()

        print("Game over!")
