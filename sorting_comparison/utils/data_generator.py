import random

class DataGenerator:
    def __init__(self, strategy):
        self.strategy = strategy  # Define a estratégia de salvamento

    def generate(self, size, filename):
        data = [random.randint(0, 1000000) for _ in range(size)]
        self.strategy.save(data, filename)
