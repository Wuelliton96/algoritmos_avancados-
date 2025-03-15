import os

class FileHandler:

    @staticmethod
    def read_file(filepath, binary=False):
        mode = 'rb' if binary else 'r'
        with open(filepath, mode) as file:
            return file.read()

    @staticmethod
    def write_file(filepath, data, binary=False):
        mode = 'wb' if binary else 'w'
        with open(filepath, mode) as file:
            file.write(data)
    
    @staticmethod
    def parse_numbers(data):
        if isinstance(data, bytes):
            data = data.decode('utf-8')
        return list(map(int, data.strip().split()))

    @staticmethod
    def format_numbers(numbers):
        return ' '.join(map(str, numbers))
