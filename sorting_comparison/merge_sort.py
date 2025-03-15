import os
from strategies.avancado.merge_sort import MergeSort
from utils.sort_context import SortContext

input_filepath = os.path.join("data", "dataset.txt")  
output_filepath = os.path.join("report", "merge_sort.txt")  

context = SortContext(MergeSort())

context.execute_sort_from_file(input_filepath, output_filepath)

print(f"Ordenação concluída! Resultado salvo em: {output_filepath}")
