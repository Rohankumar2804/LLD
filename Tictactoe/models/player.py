from Tictactoe.models.symbol import Symbol


class Player:
    name : str
    symbol : Symbol

    def __init__(self,name:str,symbol:Symbol):
        self.name = name
        self.symbol = symbol

    def get_symbol(self):
        return self.symbol
