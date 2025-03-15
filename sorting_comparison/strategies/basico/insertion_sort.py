from utils.sorting_strategy import SortingStrategy

class InsertionSort(SortingStrategy):
    def __init__(self):
        self.comparisons = 0
        self.swaps = 0

    def sort(self, array):
        n = len(array)
        for i in range(1, n):
            key = array[i]
            j = i - 1

            while j >= 0 and array[j] > key:
                self.comparisons += 1
                array[j + 1] = array[j]
                self.swaps += 1
                j -= 1

            array[j + 1] = key
            if j >= 0:
                self.comparisons += 1  # Comparação que não entrou no loop

        return array

    def get_metrics(self):
        return {"comparisons": self.comparisons, "swaps": self.swaps}
