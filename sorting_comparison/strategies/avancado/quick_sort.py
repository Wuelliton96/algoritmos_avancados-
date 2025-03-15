from utils.sorting_strategy import SortingStrategy

class QuickSort(SortingStrategy):

    def __init__(self):
        self.comparisons = 0
        self.swaps = 0

    def sort(self, array):
        if len(array) <= 1:
            return array

        pivot = array[len(array) // 2]
        left, middle, right = [], [], []

        for x in array:
            self.comparisons += 1  
            if x < pivot:
                left.append(x)
                self.swaps += 1  
            elif x > pivot:
                right.append(x)
                self.swaps += 1  
            else:
                middle.append(x)

        return self.sort(left) + middle + self.sort(right)
    
    def get_metrics(self):
        return {"comparisons": self.comparisons, "swaps": self.swaps}
