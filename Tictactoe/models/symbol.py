class Symbol:
    value : str
    def __init__(self,value):
        self.value = value

    def get_value(self):
        return self.value

    def is_equal(self,symbol):
        return self.get_value() == symbol.get_value()