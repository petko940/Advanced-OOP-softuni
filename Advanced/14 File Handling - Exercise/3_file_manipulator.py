import os

while True:
    commands = input()
    if commands == 'End':
        break

    command, file_name, *info = commands.split("-")

    if command == 'Create':
        with open(f'files/{file_name}', 'w') as file:
            pass
    elif command == 'Add':
        content = info[0]
        with open(f'files/{file_name}', 'a') as file:
            file.write(f"{content}\n")
    elif command == 'Replace':
        try:
            old_string, new_string = info[0], info[1]
            with open(f"files/{file_name}", 'r') as read:
                text = read.read()
                text = text.replace(old_string, new_string)

            with open(f"files/{file_name}", 'w') as replace:
                replace.write(text)
        except FileNotFoundError:
            print("An error occurred")

    elif command == "Delete":
        try:
            os.remove(f"files/{file_name}")
        except FileNotFoundError:
            print("An error occurred")
