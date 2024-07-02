# Написати скрипт для збереження нотаток.
import uuid

from constants import NOTE_FILE_NAMES_PATH, NOTES_FOLDER


def get_existed_notes():
    result = set()

    if NOTE_FILE_NAMES_PATH.is_file():
        with open(NOTE_FILE_NAMES_PATH) as f:
            for line in f:
                result.add(line.split(' ', maxsplit=1)[1].rstrip('\n'))

    return result


def get_note_name():
    while True:
        note_name = input('Enter a note name: ')

        if note_name in existed_notes:
            print('The note with a specified name already exists.')
        else:
            return note_name


def create_note() -> None:
    note_name = get_note_name()
    note_text = ''
    print('Please, enter a note text. When the note is entered, input [stop] on the new line')
    while True:
        note_row = input()
        if note_row == 'stop':
            do_stop = input('Do you want to stop note entering? (y/n) ')
            match do_stop:
                case 'y':
                    break
                case 'n':
                    note_text += f'{note_row}\n'
                case _:
                    print('Only "y" and "n" options are allowed')
        else:
            note_text += f'{note_row}\n'

    file_name = uuid.uuid4().hex

    with open(NOTE_FILE_NAMES_PATH, 'a') as names_file:
        names_file.write(f'{file_name} {note_name}\n')
        existed_notes.add(note_name)

    NOTES_FOLDER.mkdir(exist_ok=True)
    with open(NOTES_FOLDER / file_name, 'w') as note_file:
        note_file.write(note_text)


existed_notes = get_existed_notes()

while True:
    do_create = input('Do you want to create a new note? (y/n) ')
    match do_create:
        case 'y':
            create_note()
        case 'n':
            break
        case _:
            print('Only "y" and "n" options are allowed')
