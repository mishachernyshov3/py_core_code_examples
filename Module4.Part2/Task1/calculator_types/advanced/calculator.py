from calculator_types.advanced.logarithms import get_binary_log, get_natural_log


def calculate_result(*args, operation):
    match operation:
        case 'bin_log':
            return get_binary_log(*args)
        case 'nat_log':
            return get_natural_log(*args)
        case _:
            return None
