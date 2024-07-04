from .arithmetic import get_sum, get_subtraction
from .power import get_square, get_square_root


def calculate_result(*args, operation):
    match operation:
        case 'adding':
            return get_sum(*args)
        case 'subtraction':
            return get_subtraction(*args)
        case 'square':
            return get_square(*args)
        case 'square_root':
            return get_square_root(*args)
        case _:
            return None
