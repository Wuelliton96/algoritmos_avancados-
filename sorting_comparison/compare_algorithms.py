import os
from strategies.avancado.quick_sort import QuickSort
from strategies.avancado.merge_sort import MergeSort
from strategies.avancado.tim_sort import TimSort
from utils.performance_analyzer import PerformanceAnalyzer
from utils.file_handler import FileHandler

input_filepath = os.path.join("data", "dataset.txt")

data = FileHandler.read_file(input_filepath)
array = FileHandler.parse_numbers(data)

algorithms = [QuickSort, MergeSort, TimSort]
results = [PerformanceAnalyzer.measure_performance(algo, array) for algo in algorithms]

for result in results:
    print(result)
