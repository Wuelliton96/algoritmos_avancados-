import os
from strategies.basico.insertion_sort import InsertionSort
from utils.sort_context import SortContext

input_filepath = os.path.join("data", "dataset.txt")
output_filepath = os.path.join("report", "insertion_sort.txt")

context = SortContext(InsertionSort())

context.execute_sort_from_file(input_filepath, output_filepath)

print(f"Ordenação concluída! Resultado salvo em: {output_filepath}")
