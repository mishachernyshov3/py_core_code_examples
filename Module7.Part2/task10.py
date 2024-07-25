# Create time measuring context manager.
import time
from contextlib import contextmanager


class Timer:
    def __init__(self, block_name):
        self.__block_name = block_name
        self.__start_time = None
        self.__end_time = None
        self.__execution_time = None

    def __enter__(self):
        self.__start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__end_time = time.time()
        self.__execution_time = self.__end_time - self.__start_time
        print(f"Execution time of '{self.__block_name}': {self.__execution_time:.5f} seconds")

    @property
    def start_time(self):
        return self.__start_time

    @property
    def end_time(self):
        return self.__end_time

    @property
    def execution_time(self):
        return self.__execution_time


@contextmanager
def timer(block_name):
    start_time = time.time()
    yield
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time of '{block_name}': {execution_time:.5f} seconds")


def get_numbers_sum(max_number):
    result = 0
    for number in range(max_number + 1):
        result += number
    return result


with Timer("Getting numbers sum to 10000") as timer1:
    get_numbers_sum(10000)

with timer("Getting numbers sum to 100000") as timer2:
    get_numbers_sum(100000)
