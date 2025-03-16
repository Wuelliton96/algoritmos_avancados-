import os
import time
from opentelemetry import trace

tracer = trace.get_tracer(__name__)

class SortingStrategy:
    """Interface para a estratégia de ordenação"""
    def sort(self, data):
        pass

class ShellSort(SortingStrategy):
    """Implementação do Shell Sort"""
    def __init__(self):
        self.comparisons = 0
        self.swaps = 0

    def sort(self, arr):
        """Ordena o array usando Shell Sort"""
        n = len(arr)
        gap = n // 2  

        while gap > 0:
            for i in range(gap, n):
                temp = arr[i]
                j = i
                while j >= gap and arr[j - gap] > temp:
                    self.comparisons += 1
                    arr[j] = arr[j - gap]
                    j -= gap
                    self.swaps += 1
                arr[j] = temp
            gap //= 2  

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

    shell_sort = ShellSort()
    context = SortContext(shell_sort)

    start_time = time.time()
    sorted_data = context.execute_sort(dataset.copy())
    end_time = time.time()

    execution_time = (end_time - start_time) * 1000  

    with tracer.start_as_current_span("shell_sort_execution") as span:
        span.set_attribute("algorithm", "Shell Sort")
        span.set_attribute("dataset_size", len(dataset))
        span.set_attribute("execution_time_ms", execution_time)
        span.set_attribute("comparisons", shell_sort.comparisons)
        span.set_attribute("swaps", shell_sort.swaps)

    print(f"Shell Sort concluído em {execution_time:.2f} ms")
    print(f"Comparações: {shell_sort.comparisons}")
    print(f"Trocas: {shell_sort.swaps}")
