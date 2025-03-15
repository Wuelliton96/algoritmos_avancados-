import pickle
from utils.generator_strategy import GeneratorStrategy

class BinaryGenerator(GeneratorStrategy):

    def save(self, data, filename):
        with open(filename, 'wb') as file:
            pickle.dump(data, file)
        print(f"Arquivo salvo como {filename} (Binário)")
