#  Створити функцію, яка поверне кількість файлів із вказаним розширенням (png за змовчуванням).

file_names = [
    'colorful_fall_foliage.jpg',
    'snowy_peak.png',
    'urban_skyline_overlook.jpg',
    'canyon_view.jpg',
    'rural_farmland_sunset.jpeg',
    'coastal_view.png',
]


def get_file_names_count(files, extension="png"):
    file_names_count = 0

    for name in files:
        if name.endswith(f".{extension}"):
            file_names_count += 1

    return file_names_count
