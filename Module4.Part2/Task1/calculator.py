"""
The calculator entrypoint module.
"""
import re
import sys

from calculator_types.advanced.calculator import calculate_result as calculate_advanced_calculator_result
from calculator_types.basic.calculator import calculate_result as calculate_basic_calculator_result
from constants import (
    SUPPORTED_ADVANCED_CALCULATOR_OPERATIONS,
    SUPPORTED_OPERATIONS,
)


if __name__ == '__main__':
    operation = 'adding'
    operands = []
    unsupported_arguments = []
    invalid_operation_names = []

    for arg in sys.argv[1:]:
        if operation_match := re.fullmatch(r'^--op=([a-zA-Z_]+)$', arg):
            if (current_operation_name := operation_match.group(1)) in SUPPORTED_OPERATIONS:
                operation = current_operation_name
            else:
                invalid_operation_names.append(current_operation_name)
        elif number := re.fullmatch(r'^\d+(\.\d+)?$', arg):
            operands.append(float(arg))
        else:
            unsupported_arguments.append(arg)

    if invalid_operation_names:
        print(f'Invalid operation names: {", ".join(invalid_operation_names)}')
        sys.exit(-1)
    if unsupported_arguments:
        print(f'Unsupported arguments: {", ".join(unsupported_arguments)}')
        sys.exit(-2)

    operands = operands or [1, 2, 3]

    calculation_function = (
        calculate_advanced_calculator_result
        if operation in SUPPORTED_ADVANCED_CALCULATOR_OPERATIONS
        else calculate_basic_calculator_result
    )
    calculation_function(*operands, operation=operation)
