import os

from strategies.avancado.quick_sort import QuickSort
from strategies.avancado.merge_sort import MergeSort
from strategies.avancado.tim_sort import TimSort

from strategies.basico.bubble_sort import BubbleSort
from strategies.basico.bubble_sort_melhorado import BubbleSortMelhorado
from strategies.basico.insertion_sort import InsertionSort
from strategies.basico.selection_sort import SelectionSort

from strategies.outros_algoritmos.counting_sort import CountingSort
from strategies.outros_algoritmos.heap_sort import HeapSort
from strategies.outros_algoritmos.radix_sort import RadixSort
from strategies.outros_algoritmos.shell_sort import ShellSort

from utils.sort_context import SortContext

class SortingExecutor:
    def __init__(self, data_dir="data", report_dir="report"):
        self.data_dir = data_dir
        self.report_dir = report_dir
        os.makedirs(self.report_dir, exist_ok=True)
        self.input_filepath = os.path.join(self.data_dir, "dataset.txt")
        self.sorting_algorithms = {
            "quick_sort": QuickSort(),
            "merge_sort": MergeSort(),
            "tim_sort": TimSort(),
            "bubble_sort": BubbleSort(),
            "bubble_sort_melhorado": BubbleSortMelhorado(),
            "insertion_sort": InsertionSort(),
            "selection_sort": SelectionSort(),
            "counting_sort": CountingSort(),
            "heap_sort": HeapSort(),
            "radix_sort": RadixSort(),
            "shell_sort": ShellSort()
        }

    def execute_sorting(self):
        for algo_name, algo_instance in self.sorting_algorithms.items():
            output_filepath = os.path.join(self.report_dir, f"{algo_name}.txt")
            context = SortContext(algo_instance)
            context.execute_sort_from_file(self.input_filepath, output_filepath)
            print(f"Ordenação com {algo_name} concluída! Resultado salvo em: {output_filepath}")

if __name__ == "__main__":
    sorter = SortingExecutor()
    sorter.execute_sorting()
