import os
from strategies.basico.bubble_sort_melhorado import BubbleSortMelhorado
from utils.sort_context import SortContext

input_filepath = os.path.join("data", "dataset.txt")
output_filepath = os.path.join("report", "bubble_sort_melhorado.txt")

context = SortContext(BubbleSortMelhorado())

context.execute_sort_from_file(input_filepath, output_filepath)

print(f"Ordenação concluída! Resultado salvo em: {output_filepath}")
