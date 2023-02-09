import pyfiglet


def custom_input(word):
    art = pyfiglet.figlet_format(word)
    print(art)


custom_input(input())
