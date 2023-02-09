from module import *

while True:
    command = input()
    event, *info = command.split()
    if event.startswith("Stop"):
        break
    if event.startswith("Create"):
        print(fibonacci_sequence(int(info[-1])))
    elif event.startswith("Locate"):
        print(check_sequence(int(info[-1])))
