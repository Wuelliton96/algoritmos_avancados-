from utils.sorting_strategy import SortingStrategy

class TimSort(SortingStrategy):

    RUN = 32 

    def __init__(self):
        self.comparisons = 0
        self.swaps = 0

    def sort(self, array):
        n = len(array)

        for start in range(0, n, self.RUN):
            end = min(start + self.RUN, n)
            self._insertion_sort(array, start, end)

        size = self.RUN
        while size < n:
            for left in range(0, n, 2 * size):
                mid = min(n, left + size)
                right = min(n, left + 2 * size)
                self._merge(array, left, mid, right)
            size *= 2

        return array

    def _insertion_sort(self, array, left, right):
        for i in range(left + 1, right):
            temp = array[i]
            j = i - 1
            while j >= left:
                self.comparisons += 1  
                if array[j] > temp:
                    array[j + 1] = array[j]
                    j -= 1
                    self.swaps += 1 
                else:
                    break
            array[j + 1] = temp

    def _merge(self, array, left, mid, right):
        left_part = array[left:mid]
        right_part = array[mid:right]
        i = j = 0
        k = left

        while i < len(left_part) and j < len(right_part):
            self.comparisons += 1  
            if left_part[i] < right_part[j]:
                array[k] = left_part[i]
                i += 1
            else:
                array[k] = right_part[j]
                j += 1
            self.swaps += 1  
            k += 1

        while i < len(left_part):
            array[k] = left_part[i]
            i += 1
            k += 1

        while j < len(right_part):
            array[k] = right_part[j]
            j += 1
            k += 1

    def get_metrics(self):
        return {"comparisons": self.comparisons, "swaps": self.swaps}
