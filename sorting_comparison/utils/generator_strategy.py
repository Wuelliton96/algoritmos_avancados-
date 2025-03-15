from abc import ABC, abstractmethod

class GeneratorStrategy(ABC):
    
    @abstractmethod
    def save(self, data, filename):
        pass
