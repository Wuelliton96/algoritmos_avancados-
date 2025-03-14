from sort_algorithms.sorting_strategy import SortingStrategy

class BubbleSort(SortingStrategy):
    
    def sort(self, data):
        n = len(data)
        comparisons, swaps = 0, 0
        
        for i in range(n):
            swapped = False
            for j in range(0, n-i-1):
                comparisons += 1
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
                    swaps += 1
                    swapped = True
            if not swapped:
                break
        
        return data, comparisons, swaps
