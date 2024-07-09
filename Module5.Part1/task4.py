# Створити список працівників відділу.
from collections import defaultdict, namedtuple


DepartmentInfo = namedtuple('DepartmentInfo', ['department', 'employee'])


dep_info_list = [
    DepartmentInfo('Sales', 'John Doe'),
    DepartmentInfo('Sales', 'Martin Smith'),
    DepartmentInfo('Accounting', 'Jane Doe'),
    DepartmentInfo('Marketing', 'Elizabeth Smith'),
    DepartmentInfo('Marketing', 'Adam Doe')
]
department_employees = defaultdict(list)

for department_info in dep_info_list:
    department_employees[department_info.department].append(department_info.employee)


print(department_employees)
