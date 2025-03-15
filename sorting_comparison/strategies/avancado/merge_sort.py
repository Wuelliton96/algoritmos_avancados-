from utils.sorting_strategy import SortingStrategy

class MergeSort(SortingStrategy):
    def __init__(self):
        self.comparisons = 0
        self.swaps = 0

    def sort(self, array):
        if len(array) <= 1:
            return array

        mid = len(array) // 2
        left_half = self.sort(array[:mid])
        right_half = self.sort(array[mid:])

        return self._merge(left_half, right_half)

    def _merge(self, left, right):
        sorted_array = []
        i = j = 0

        while i < len(left) and j < len(right):
            self.comparisons += 1  
            if left[i] < right[j]:
                sorted_array.append(left[i])
                i += 1
            else:
                sorted_array.append(right[j])
                j += 1
            self.swaps += 1  

        sorted_array.extend(left[i:])
        sorted_array.extend(right[j:])
        return sorted_array

    def get_metrics(self):
        return {"comparisons": self.comparisons, "swaps": self.swaps}
