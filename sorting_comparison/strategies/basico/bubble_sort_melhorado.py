from utils.sorting_strategy import SortingStrategy

class BubbleSortMelhorado(SortingStrategy):
    def __init__(self):
        self.comparisons = 0
        self.swaps = 0

    def sort(self, array):
        n = len(array)
        for i in range(n):
            swapped = False
            last_swap_index = 0  # Índice do último elemento trocado

            for j in range(0, n - i - 1):
                self.comparisons += 1
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
                    self.swaps += 1
                    swapped = True
                    last_swap_index = j + 1  # Marca a posição da última troca

            if not swapped:
                break  # Sai se o array já estiver ordenado

            n = last_swap_index  # Reduz o intervalo da próxima varredura

        return array

    def get_metrics(self):
        return {"comparisons": self.comparisons, "swaps": self.swaps}
