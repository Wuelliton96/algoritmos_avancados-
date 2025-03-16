import os
import time
from opentelemetry import trace

tracer = trace.get_tracer(__name__)

class SortingStrategy:
    """Interface para a estratégia de ordenação"""
    def sort(self, data):
        pass

class CountingSort(SortingStrategy):
    """Implementação do Counting Sort"""
    def __init__(self):
        self.comparisons = 0
        self.swaps = 0  
    def sort(self, arr):
        """Ordena o array usando Counting Sort"""
        if not arr:
            return arr

        max_value = max(arr)  
        min_value = min(arr) 
        range_of_elements = max_value - min_value + 1  

        count = [0] * range_of_elements
        output = [0] * len(arr)

        for num in arr:
            count[num - min_value] += 1

        for i in range(1, len(count)):
            count[i] += count[i - 1]

        for num in reversed(arr):
            output[count[num - min_value] - 1] = num
            count[num - min_value] -= 1

        return output

class SortContext:
    """Contexto que usa uma estratégia de ordenação"""
    def __init__(self, strategy: SortingStrategy):
        self.strategy = strategy

    def execute_sort(self, data):
        return self.strategy.sort(data)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  
DATA_FILE = os.path.join(BASE_DIR, "..", "..", "data", "dataset.txt")  

def load_data(filename):
    """Carrega os dados do arquivo"""
    with open(filename, "r") as file:
        return [int(line.strip()) for line in file.readlines()]

if __name__ == "__main__":
    if not os.path.exists(DATA_FILE):
        print(f"Erro: O arquivo {DATA_FILE} não foi encontrado. Execute o gerador de dados primeiro.")
        exit(1)

    dataset = load_data(DATA_FILE)

    counting_sort = CountingSort()
    context = SortContext(counting_sort)

    start_time = time.time()
    sorted_data = context.execute_sort(dataset.copy())
    end_time = time.time()

    execution_time = (end_time - start_time) * 1000  

    with tracer.start_as_current_span("counting_sort_execution") as span:
        span.set_attribute("algorithm", "Counting Sort")
        span.set_attribute("dataset_size", len(dataset))
        span.set_attribute("execution_time_ms", execution_time)
        span.set_attribute("comparisons", counting_sort.comparisons)
        span.set_attribute("swaps", counting_sort.swaps)

    print(f"Counting Sort concluído em {execution_time:.2f} ms")
    print(f"Comparações: {counting_sort.comparisons}")  
    print(f"Trocas: {counting_sort.swaps}")  
