
import os
from strategies.avancado.quick_sort import QuickSort
from utils.sort_context import SortContext

# Definir caminhos dos arquivos
input_filepath = os.path.join("data", "dataset.txt")
output_filepath = os.path.join("report", "quick_sort.txt")

# Criar o contexto e definir o algoritmo como QuickSort
context = SortContext(QuickSort())

# Executar a ordenação baseada no arquivo de entrada
context.execute_sort_from_file(input_filepath, output_filepath)

print(f"Ordenação concluída! Resultado salvo em: {output_filepath}")
