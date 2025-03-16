import os
import time
from opentelemetry import trace

tracer = trace.get_tracer(__name__)

class SortingStrategy:
    """Interface para a estratégia de ordenação"""
    def sort(self, data):
        pass

class RadixSort(SortingStrategy):
    """Implementação do Radix Sort"""
    def __init__(self):
        self.comparisons = 0
        self.swaps = 0  

    def counting_sort(self, arr, exp):
        """Ordenação estável baseada no dígito específico (exp)"""
        n = len(arr)
        output = [0] * n
        count = [0] * 10  

        for num in arr:
            index = (num // exp) % 10
            count[index] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        i = n - 1
        while i >= 0:
            index = (arr[i] // exp) % 10
            output[count[index] - 1] = arr[i]
            count[index] -= 1
            i -= 1

        return output

    def sort(self, arr):
        """Ordena o array usando Radix Sort"""
        if not arr:
            return arr

        max_value = max(arr)  
        exp = 1  

        while max_value // exp > 0:
            arr = self.counting_sort(arr, exp)
            exp *= 10

        return arr

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

    radix_sort = RadixSort()
    context = SortContext(radix_sort)

    start_time = time.time()
    sorted_data = context.execute_sort(dataset.copy())
    end_time = time.time()

    execution_time = (end_time - start_time) * 1000 

    with tracer.start_as_current_span("radix_sort_execution") as span:
        span.set_attribute("algorithm", "Radix Sort")
        span.set_attribute("dataset_size", len(dataset))
        span.set_attribute("execution_time_ms", execution_time)
        span.set_attribute("comparisons", radix_sort.comparisons)
        span.set_attribute("swaps", radix_sort.swaps)

    print(f"Radix Sort concluído em {execution_time:.2f} ms")
    print(f"Comparações: {radix_sort.comparisons}")  
    print(f"Trocas: {radix_sort.swaps}")  
