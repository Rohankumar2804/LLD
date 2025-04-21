from typing import List


class Board:
    grid : List
    size : int

    def __init__(self,size):
        self.size = size
        self.grid = [[None for _ in range(self.size)] for _ in range(self.size)]

    def is_empty(self,row,col):
        return self.grid[row][col] is None

    def is_full(self):
        return all( col is not None  for row in self.grid for col in row)

    def update_cell(self, row, col, symbol):
        self.grid[row][col] = symbol.get_value()

    def display(self):
        for row in self.grid:
            res = '|'
            for col in row:
                if col:
                    res+=col
                else:
                    res += ' '
                res+='|'
            print(res)
            print('_'* (2*len(self.grid) + 1))


    def is_winner(self,symbol):
        for i in range(len(self.grid)):
            if all(sys == symbol for sys in self.grid[i]):
                return True
            if all(symbol == self.grid[j][i] for j in range(len(self.grid[i]))):
                return True

        if all(symbol == self.grid[i][i] for i in range(len(self.grid))):
            return True

        if all(symbol == self.grid[i][self.size-i-1] for i in range(len(self.grid))):
            return True

        return False



