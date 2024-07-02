# Поекспериментувати із максимально можливою кількістю відкритих файлів одночасно.

from pathlib import Path

files = [open(Path('file_experiment') / f'file-{n}.txt', mode='w') for n in range(1_000_000_000_000)]
