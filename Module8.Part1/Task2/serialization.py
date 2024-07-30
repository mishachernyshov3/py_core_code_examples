# Реалізувати збереження та зчитування збережених записів із файлу за допомогою модуля pickle.
import pickle
from contextlib import contextmanager
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


DATA_SEPARATOR = "|"
RECORDS_FILE_PATH = Path("records.pickle")
DATE_FORMAT = "%d.%m"


@dataclass
class Record:
    name: str
    phone: str
    birthday: datetime

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Birthday: {self.birthday.strftime(DATE_FORMAT)}"


def add_new_record(records_list):
    name = input("Enter a name: ")
    phone = input("Enter the phone number: ")
    birthday = datetime.strptime(input("Enter the birthday (DD.MM): "), DATE_FORMAT)

    records_list.append(Record(name=name, phone=phone, birthday=birthday))


def save_records(records_list):
    with open(RECORDS_FILE_PATH, "wb") as records_file:
        pickle.dump(records_list, records_file)


def load_records():
    records_list = []
    if RECORDS_FILE_PATH.is_file():
        with open(RECORDS_FILE_PATH, "rb") as records_file:
            records_list = pickle.load(records_file)
    return records_list


@contextmanager
def record_manager():
    records_list = load_records()
    try:
        yield records_list
    finally:
        save_records(records_list)


if __name__ == "__main__":
    with record_manager() as records:
        while True:
            does_add_record = input("Do you want to add a new record (y/n)? ").lower()
            if does_add_record == "y":
                add_new_record(records)
            elif does_add_record == "n":
                break
            else:
                print("Incorrect input. Try again.")

        if records:
            print("Your records:")
            for record in records:
                print(record)
