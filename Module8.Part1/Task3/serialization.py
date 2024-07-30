# Реалізувати збереження та зчитування збережених записів із файлу за допомогою модуля json.
import json
from contextlib import contextmanager
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


DATA_SEPARATOR = "|"
RECORDS_FILE_PATH = Path("records.json")
DATE_FORMAT = "%d.%m"


@dataclass
class Record:
    name: str
    phone: str
    birthday: datetime

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Birthday: {self.birthday.strftime(DATE_FORMAT)}"


class RecordEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Record):
            return {
                "name": obj.name,
                "phone": obj.phone,
                "birthday": obj.birthday.strftime(DATE_FORMAT),
            }

        return super().default(obj)


class RecordDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, object_hook=self.object_hook, **kwargs)

    def object_hook(self, dct):
        if set(dct.keys()) == {"name", "phone", "birthday"}:
            return Record(
                name=dct["name"],
                phone=dct["phone"],
                birthday=datetime.strptime(dct["birthday"], DATE_FORMAT),
            )
        return dct


def add_new_record(records_list):
    name = input("Enter a name: ")
    phone = input("Enter the phone number: ")
    birthday = datetime.strptime(input("Enter the birthday (DD.MM): "), DATE_FORMAT)

    records_list.append(Record(name=name, phone=phone, birthday=birthday))


def save_records(records_list):
    with open(RECORDS_FILE_PATH, "w") as records_file:
        json.dump(records_list, records_file, cls=RecordEncoder, ensure_ascii=False, indent=4)


def load_records():
    records_list = []
    if RECORDS_FILE_PATH.is_file():
        with open(RECORDS_FILE_PATH) as records_file:
            records_list = json.load(records_file, cls=RecordDecoder)
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
