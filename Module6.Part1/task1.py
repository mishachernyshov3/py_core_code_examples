# Створити генератор звітів по успішності учнів групи
import json
import datetime
from collections import defaultdict


def get_data_from_db():
    return """
[
    ["Ava Cooper", "Python Core", 5, 10, "12.05.2024"],
    ["Isaac Carter", "Python Web Development", 3, 4, "10.03.2024"],
    ["Ava Cooper", "Python Core", 2, 2, "24.04.2024"],
    ["Olivia Richardson", "Python Web Development", 5, 7, "04.04.2024"],
    ["Noah Harris", "Python Core", 1, 5, "10.05.2024"],
    ["Lucas Bennett", "Python Core", 0, 3, "01.06.2024"],
    ["Noah Harris", "Python Core", 10, 10, "06.05.2024"]
]
"""


class ReportGenerator:
    def generate_report(self, group=None):
        raise NotImplementedError


class CsvReportGenerator(ReportGenerator):
    def __init__(self, data):
        self._data = data

    def _filter_data(self, group, from_date, to_date):
        filtered_data = []

        for row in self._data:
            if group is not None and row["student"].group != group:
                continue

            if from_date is not None and row["grade"] < from_date:
                continue

            if to_date is not None and row["grade"] > to_date:
                continue

            filtered_data.append(row)

        self._data = filtered_data

    def _calculate_average_grade(self):
        student_grades = defaultdict(list)

        for row in self._data:
            student_grades[row["student"].name].append(row["grade"].get_value())

        return {
            student: sum(grades) / len(grades)
            for student, grades in student_grades.items()
        }

    def generate_report(self, group=None, from_date=None, to_date=None):
        self._filter_data(group, from_date, to_date)

        with open("output.csv", "w") as file:
            file.write("Student Name,Grade")

            for student, avg_grade in self._calculate_average_grade().items():
                file.write(",".join([student, str(round(avg_grade, 2))]))
                file.write("\n")


class RequestHandler:
    def generate_grade_report(self, **report_params):
        student_data = get_data_from_db()
        serializer = StudentDataSerializer(student_data)
        deserialized_data = serializer.deserialize_user_data()
        CsvReportGenerator(deserialized_data).generate_report(**report_params)


class Student:
    def __init__(self, name, group):
        self.name = name
        self.group = group


class Grade:
    def __init__(self, set_value, max_value, getting_time):
        self.set_value = set_value
        self.max_value = max_value
        self.getting_time = getting_time

    def get_value(self):
        return self.set_value / self.max_value


class StudentDataSerializer:
    def __init__(self, student_data):
        self._student_data = student_data

    def deserialize_user_data(self):
        processed_data = json.loads(self._student_data)

        return [
            {
                "student": Student(data_item[0], data_item[1]),
                "grade": Grade(
                    data_item[2],
                    data_item[3],
                    datetime.datetime.strptime(data_item[4], "%d.%m.%Y"),
                ),
            }
            for data_item in processed_data
        ]


RequestHandler().generate_grade_report(group="Python Web Development")
