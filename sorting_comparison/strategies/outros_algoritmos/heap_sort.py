import os
import time
from opentelemetry import trace

tracer = trace.get_tracer(__name__)

class SortingStrategy:
    """Interface para a estratégia de ordenação"""
    def sort(self, data):
        pass

    def get_metrics(self):
        """Retorna métricas padrão para estratégias de ordenação"""
        return {
            "comparisons": 0,
            "swaps": 0
        }

class HeapSort(SortingStrategy):
    """Implementação do Heap Sort"""
    def __init__(self):
        self.comparisons = 0
        self.swaps = 0

    def heapify(self, arr, n, i):
        """Função auxiliar para garantir a propriedade de heap"""
        largest = i  
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n:
            self.comparisons += 1
            if arr[left] > arr[largest]:
                largest = left

        if right < n:
            self.comparisons += 1
            if arr[right] > arr[largest]:
                largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  
            self.swaps += 1
            self.heapify(arr, n, largest)

    def sort(self, arr):
        """Ordena o array usando Heap Sort"""
        n = len(arr)

        # Construção do heap (heapify para cada nó não folha)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)

        # Extração dos elementos do heap um por um
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  
            self.swaps += 1
            self.heapify(arr, i, 0)

        return arr

    def get_metrics(self):
        """Retorna métricas detalhadas do Heap Sort"""
        return {
            "comparisons": self.comparisons,
            "swaps": self.swaps
        }

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

    heap_sort = HeapSort()
    context = SortContext(heap_sort)

    start_time = time.time()
    sorted_data = context.execute_sort(dataset.copy())
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000  

    metrics = heap_sort.get_metrics()

    with tracer.start_as_current_span("heap_sort_execution") as span:
        span.set_attribute("algorithm", "Heap Sort")
        span.set_attribute("dataset_size", len(dataset))
        span.set_attribute("execution_time_ms", execution_time)
        for key, value in metrics.items():
            span.set_attribute(key, value)

    print(f"Heap Sort concluído em {execution_time:.2f} ms")
    print(f"Métricas:\n" + "\n".join(f"  {key}: {value}" for key, value in metrics.items()))
