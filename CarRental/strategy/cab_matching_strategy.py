from abc import ABC,abstractmethod

class CabMatchingStrategy(ABC):

    @abstractmethod
    def find_cabs(self,cabs,location):
        pass