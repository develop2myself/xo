import sys
from start_game import start_game


def menu():
    response = int(input("Игра Крестики-Нолики"
                         "1. Начать игру"
                         "2. Выход"))
    if response == 1:
        return start_game()
    elif response == 2:
        return sys.exit()
    else:
        print("Некорректный ввод!")
        menu()
