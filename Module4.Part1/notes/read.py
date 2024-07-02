# Написати скрипт для зчитування нотаток.
from constants import INVALID_NOTE_INDEX_MESSAGE, NOTE_FILE_NAMES_PATH, NOTES_FOLDER


def build_note_file_mapping():
    result = {}

    if NOTE_FILE_NAMES_PATH.is_file():
        with open(NOTE_FILE_NAMES_PATH) as f:
            for line in f:
                file_name, note_name = line.split(' ', maxsplit=1)
                note_name = note_name.rstrip('\n')
                result[note_name] = file_name

    return result


def print_notes_list(note_file_mapping):
    for index, note_name in enumerate(note_file_mapping.keys()):
        print(f'{index + 1}) {note_name}')


def get_note_index(note_file_mapping):
    while True:
        note_number_string = input('Enter a note number: ')
        if note_number_string.isnumeric():
            note_index = int(note_number_string) - 1
            if 0 <= note_index < len(note_file_mapping):
                return note_index
        print(INVALID_NOTE_INDEX_MESSAGE)


def read_note(note_file_mapping):
    note_index = get_note_index(note_file_mapping)
    note_file_name = list(note_file_mapping.values())[note_index]

    with open(NOTES_FOLDER / note_file_name) as f:
        for line in f:
            print(line, end='')


note_name_to_file_name_mapping = build_note_file_mapping()

while True:
    print('Notes list: ')
    print_notes_list(note_name_to_file_name_mapping)
    do_read = input('Do you want to read a note? (y/n) ')
    match do_read:
        case 'y':
            read_note(note_name_to_file_name_mapping)
        case 'n':
            break
        case _:
            print('Only "y" and "n" options are allowed')
