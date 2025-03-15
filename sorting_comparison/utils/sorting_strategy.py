# utils/sorting_strategy.py
from abc import ABC, abstractmethod

class SortingStrategy(ABC):

    @abstractmethod
    def sort(self, array):
        pass
