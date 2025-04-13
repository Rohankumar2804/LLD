from abc import ABC,abstractmethod

class PriceCalculationStrategy(ABC):

    @abstractmethod
    def calculate_price(self,from_location,to_location):
        pass