import os
import concurrent.futures

from strategies.avancado.quick_sort import QuickSort
from strategies.avancado.merge_sort import MergeSort
from strategies.avancado.tim_sort import TimSort
from strategies.basico.bubble_sort import BubbleSort
from strategies.basico.bubble_sort_melhorado import BubbleSortMelhorado
from strategies.basico.selection_sort import SelectionSort
from strategies.basico.insertion_sort import InsertionSort
from strategies.outros_algoritmos.counting_sort import CountingSort
from strategies.outros_algoritmos.heap_sort import HeapSort
from strategies.outros_algoritmos.radix_sort import RadixSort
from strategies.outros_algoritmos.shell_sort import ShellSort

from utils.performance_analyzer import PerformanceAnalyzer
from utils.file_handler import FileHandler
from report import SortingExecutor

# OpenTelemetry com OTLP
from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter

# Configuração do OTLP (sem warnings)
resource = Resource.create({"service.name": "sorting-benchmark"})
provider = TracerProvider(resource=resource)
trace.set_tracer_provider(provider)

otlp_exporter = OTLPSpanExporter(endpoint="http://localhost:4317", insecure=True)
provider.add_span_processor(BatchSpanProcessor(otlp_exporter))

tracer = trace.get_tracer(__name__)

# Caminho do dataset
input_filepath = os.path.join("data", "dataset.txt")
data = FileHandler.read_file(input_filepath)
array = FileHandler.parse_numbers(data)

# Lista dos algoritmos a serem executados
algorithms = [
    QuickSort, MergeSort, TimSort,
    BubbleSort, BubbleSortMelhorado,
    SelectionSort, InsertionSort,
    CountingSort, HeapSort, RadixSort, ShellSort
]

# Função que roda cada algoritmo com métricas e trace
def run_algorithm(algo_class):
    with tracer.start_as_current_span(f"run-{algo_class.__name__}") as span:
        try:
            result = PerformanceAnalyzer.measure_performance(algo_class, list(array))  # usa cópia do array
            span.set_attribute("algorithm", algo_class.__name__)
            span.set_attribute("dataset_size", len(array))
            span.set_attribute("execution_time_ms", result["execution_time_ms"])
            span.set_attribute("comparisons", result["comparisons"])
            span.set_attribute("swaps", result["swaps"])
            return {
                "algorithm": algo_class.__name__,
                "execution_time_ms": result["execution_time_ms"],
                "comparisons": result["comparisons"],
                "swaps": result["swaps"],
            }
        except Exception as e:
            print(f"Erro no algoritmo {algo_class.__name__}: {e}")
            return {
                "algorithm": algo_class.__name__,
                "execution_time_ms": None,
                "comparisons": None,
                "swaps": None,
            }


# Executa todos os algoritmos paralelamente (apenas 1 vez cada)
with concurrent.futures.ThreadPoolExecutor() as executor:
    results = list(executor.map(run_algorithm, algorithms))

# Exibe os resultados
print("\n====== RESULTADOS DOS ALGORITMOS (Execução Única e Paralela) ======")
for result in results:
    print(f"\nAlgoritmo: {result['algorithm']}")
    print(f"Tempo de execução: {result['execution_time_ms']} ms")
    print(f"Comparações: {result['comparisons']}")
    print(f"Trocas: {result['swaps']}")

# Gera relatório final
txt_sorter = SortingExecutor()
txt_sorter.execute_sorting()