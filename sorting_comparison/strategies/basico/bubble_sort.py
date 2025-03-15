from utils.sorting_strategy import SortingStrategy

class BubbleSort(SortingStrategy):
    def __init__(self):
        self.comparisons = 0
        self.swaps = 0

    def sort(self, array):
        n = len(array)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                self.comparisons += 1
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
                    self.swaps += 1
                    swapped = True
            if not swapped:
                break  # Otimização para sair caso o array já esteja ordenado
        return array

    def get_metrics(self):
        return {"comparisons": self.comparisons, "swaps": self.swaps}

