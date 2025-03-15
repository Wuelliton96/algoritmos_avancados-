from utils.text_generator import TextGenerator
from utils.binary_generator import BinaryGenerator
from utils.data_generator import DataGenerator

if __name__ == "__main__":
    tamanho = int(input("Digite o tamanho do conjunto de dados (ex: 1000, 10000, 100000): "))
    formato = input("Escolha o formato (texto/binário): ").strip().lower()

    if formato == "texto":
        strategy = TextGenerator()
        filename = "data/dataset.txt"
    elif formato == "binário":
        strategy = BinaryGenerator()
        filename = "data/dataset.bin"
    else:
        print("Formato inválido. Escolha entre 'texto' ou 'binário'.")
        exit(1)

    generator = DataGenerator(strategy)
    generator.generate(tamanho, filename)
