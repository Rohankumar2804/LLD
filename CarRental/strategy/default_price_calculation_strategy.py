from abc import ABC,abstractmethod

from CarRental.models.location import Location
from CarRental.strategy.price_calculation_strategy import PriceCalculationStrategy


class DefaultPriceCalculationStrategy(PriceCalculationStrategy):
    PER_KM_RATE = 10.0
    @classmethod
    def calculate_price(cls,from_location : Location,to_location:Location):
        return cls.PER_KM_RATE * from_location.get_distance(to_location)