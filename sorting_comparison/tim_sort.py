import os
from strategies.avancado.tim_sort import TimSort
from utils.sort_context import SortContext

input_filepath = os.path.join("data", "dataset.txt")  
output_filepath = os.path.join("report", "tim_sort.txt")  

context = SortContext(TimSort())

context.execute_sort_from_file(input_filepath, output_filepath)

print(f"Ordenação concluída! Resultado salvo em: {output_filepath}")
