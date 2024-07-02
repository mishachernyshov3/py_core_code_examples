# Згенерувати заглушки файлів для автоперевірок.
import shutil
from pathlib import Path

solution_dir = Path('solution')
example_script_path = Path('res/example.py')


structure = [
    {
        'name': 'Module1',
        'task_count': 5,
    },
    {
        'name': 'Module2',
        'task_count': 2,
    },
    {
        'name': 'Module3',
        'task_count': 3,
    },
]

solution_dir.mkdir(exist_ok=True)

for item in structure:
    module_path = solution_dir / item['name']
    module_path.mkdir(exist_ok=True)
    module_example_script_path = module_path / example_script_path.name

    for index, task in enumerate(range(item['task_count'])):
        shutil.copy2(example_script_path, module_path)
        task_file_path = module_path / f'task_{index + 1}.{example_script_path.suffix}'
        shutil.move(module_example_script_path, task_file_path)

shutil.make_archive('compressed_solution', 'zip', root_dir=solution_dir)
shutil.rmtree(solution_dir)
