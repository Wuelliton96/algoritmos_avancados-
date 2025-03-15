from utils.generator_strategy import GeneratorStrategy

class TextGenerator(GeneratorStrategy):

    def save(self, data, filename):
        with open(filename, 'w') as file:
            for number in data:
                file.write(f"{number}\n")
        print(f"Arquivo salvo como {filename} (Texto)")
