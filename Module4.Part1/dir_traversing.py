# Вивести усі файли із поточної директорії і її піддиректорій з вказаним розширенням.
from pathlib import Path

from colorama import Fore, Back, Style


def print_dir_content(current_dir=Path('.'), shift=0, extensions_colors=None):
    if extensions_colors is None:
        extensions_colors = {'.py': Fore.YELLOW + Back.BLUE}

    for path in current_dir.iterdir():
        if path.is_dir():
            print(' ' * shift + f'- {path.name}')
            print_dir_content(path, shift + 2)
        elif path.suffix in extensions_colors:
            styles = extensions_colors[path.suffix]
            print(' ' * shift + styles + path.name + Style.RESET_ALL)


print_dir_content()
