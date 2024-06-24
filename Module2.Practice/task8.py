# Створити функцію, яка приймає рядок - консольну команду
# Можливі команди:
# show - вивести рядок "List all files and directories: "
# remove file1 file2 --ask - Вивести "Please confirm: Removing files: file1 file2"
# remove file1 file2 - Вивести "Removing files: file1 file2"
# Інакше - вивести "Command not recognized"

def file_handler_v2(command):
    match command.split():
        case ['show']:
            print('List all files and directories: ')
        case ['remove' | 'delete', *files] if '--ask' in files:
            del_files = [f for f in files if len(f.split('.'))>1]
            print('Please confirm: Removing files: {}'.format(del_files))
        case ['remove' | 'delete', *files]:
            print('Removing files: {}'.format(files))
        case _:
            print('Command not recognized')
