# Упевнитися, що __getstate__ і __setstate__ дозволяють копіювати екземпляри класу CsvDictReader, що містить значеннями
# полів файли.
import copy
from pathlib import Path


class CsvDictReader:
    def __init__(self, file_path, encoding="utf-8", delimiter=","):
        self.__file_path = file_path
        self.__encoding = encoding
        self.__file = open(file_path, encoding=encoding)
        self.__fieldnames = self.__file.readline().rstrip().split(delimiter)
        self.__read_rows_count = 1
        self.__data = []
        self.__delimiter = delimiter

    @property
    def file_path(self):
        return self.__file_path

    @property
    def fieldnames(self):
        return self.__fieldnames

    @property
    def data(self):
        return self.__data

    @property
    def delimiter(self):
        return self.__delimiter

    def read_row(self):
        row_data = self.__file.readline().rstrip("\n").split(self.delimiter)
        if row_data != [""]:
            row_dict = dict(zip(self.__fieldnames, row_data))
            self.data.append(row_dict)
            self.__read_rows_count += 1
            return row_dict
        return None

    def close(self):
        self.__file.close()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

    def __getstate__(self):
        return {
            key: value for key, value in self.__dict__.items()
            if key != "_CsvDictReader__file"
        }

    def __setstate__(self, state):
        self.__dict__ = state
        self.__file = open(self.__file_path, encoding=self.__encoding)

        for _ in range(self.__read_rows_count):
            self.__file.readline()


if __name__ == "__main__":
    with CsvDictReader(Path("records.csv")) as reader:
        reader.read_row()

        reader_copy = copy.deepcopy(reader)

        print(reader.read_row())
        print(reader.data)

        print(reader_copy.read_row())
        print(reader_copy.data)

        reader_copy.close()
