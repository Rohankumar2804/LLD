from CarRental.strategy.cab_matching_strategy import CabMatchingStrategy


class DefaultMatchingCab(CabMatchingStrategy):

    def find_cabs(self,cabs,location):
        return min(cabs, key=lambda cab: cab.location.get_distance(location), default=None)
