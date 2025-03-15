from utils.sorting_strategy import SortingStrategy

class SelectionSort(SortingStrategy):
    def __init__(self):
        self.comparisons = 0
        self.swaps = 0

    def sort(self, array):
        n = len(array)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                self.comparisons += 1
                if array[j] < array[min_index]:
                    min_index = j

            if min_index != i:
                array[i], array[min_index] = array[min_index], array[i]
                self.swaps += 1

        return array

    def get_metrics(self):
        return {"comparisons": self.comparisons, "swaps": self.swaps}
