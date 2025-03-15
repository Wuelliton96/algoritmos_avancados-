from utils.file_handler import FileHandler

class SortContext:

    def __init__(self, strategy):
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def execute_sort_from_file(self, input_filepath, output_filepath, binary=False):
        data = FileHandler.read_file(input_filepath, binary)
        numbers = FileHandler.parse_numbers(data)
        sorted_numbers = self._strategy.sort(numbers)
        FileHandler.write_file(output_filepath, FileHandler.format_numbers(sorted_numbers), binary)
