import time

class PerformanceAnalyzer:

    @staticmethod
    def measure_performance(strategy, array, iterations=10):
        total_time = 0
        total_comparisons = 0
        total_swaps = 0

        for _ in range(iterations):
            strategy_instance = strategy()
            start_time = time.perf_counter()
            strategy_instance.sort(array.copy())  
            elapsed_time = (time.perf_counter() - start_time) * 1000  
            metrics = strategy_instance.get_metrics()

            total_time += elapsed_time
            total_comparisons += metrics["comparisons"]
            total_swaps += metrics["swaps"]

        return {
            "algoritmo": strategy.__name__,
            "tempo_médio_ms": total_time / iterations,
            "comparações_médias": total_comparisons / iterations,
            "trocas_médias": total_swaps / iterations
        }
