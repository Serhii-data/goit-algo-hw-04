from colorama import Fore, Style, Cursor
from pathlib import Path
import sys


def argv_to_path():
    """
    Отримує шлях з аргументів з командного рядка
    :return: Шлях або None, при відсутності аргументів
    """
    if len(sys.argv) > 1:
        return Path(sys.argv[1])

    print("Pass arguments at startup")
    return None


def visual_print(name_directory_or_file: str, level: int = 0, is_dir: bool = True):
    """
    Виводить ім'я файлу/директорії у кольоровому вигляді та відступом
    :param name_directory_or_file: Ім'я директорії/файлу
    :param level: Поточний рівень вкладеності
    :param is_dir: Директорія чи файл
    :return: None
    """
    style_reset = Style.RESET_ALL
    forward_cursor = Cursor.FORWARD(
        level * 4) if level else ""  # Відступ для напису

    if is_dir:  # Вибір кольору
        name_directory_or_file += "/"
        color = Fore.BLUE
    else:
        color = Fore.GREEN

    print(color + forward_cursor + name_directory_or_file + style_reset)


def parse_folder(path: Path, level: int = 0):
    """
    Рекурсивно виводить структуру директорії у вигляді дерева.
    :param path: Шлях до директорії / файлу
    :param level: Поточний рівень вкладеності
    """
    try:
        # Створення винятків
        if not path.exists():
            raise Exception(f"Directory {path} not found.")
        if path.is_file() and level == 0:
            raise Exception(f"Root {path} cannot be a file")

        if level == 0:
            visual_print(path.name)

        for fl in path.iterdir():  # Проходимо всю директорію
            is_dir = fl.is_dir()
            visual_print(fl.name, level=level + 1, is_dir=is_dir)
            if is_dir: # Якщо директорія - рекурсивно проходимо
                parse_folder(path=fl, level=level + 1)
    # Обробка винятків
    except FileNotFoundError:
        print(f"Directory or file {path} not found.")
    except PermissionError:
        print(f"No access rights to the file/directory {path}")
    except Exception as error:
        print(f"{error}")


if __name__ == "__main__":

    path_string = argv_to_path()
    if path_string:
        parse_folder(path_string)