from colorama import Fore, Style, Cursor
from pathlib import Path
import sys


def argv_to_path():
    """
    Отримує шлях з аргументів з командного рядка
    :return: Абсолютний шлях або None, якщо аргумент не передано
    """
    if len(sys.argv) > 1:
        return Path(sys.argv[1])

    print("Pass arguments at startup")
    return None


def visual_print(name_directory_or_file: str, level: int = 0, is_dir: bool = True):
    """
    Виводить ім'я файлу/директорії у кольоровому вигляді та відступом
    :param name_directory_or_file: Ім'я директорії/файлу
    :param level: Вказує рівень директорії відносно батьківської директорії
    :param is_dir: Вказує чи це директорія чи файл
    :return: None
    """
    style_reset = Style.RESET_ALL
    forward_cursor = Cursor.FORWARD(
        level * 4) if level else ""  # Відступ напису поточної директорії/файлу від кореня

    if is_dir:  # Колір для ім'я директорії або файлу
        name_directory_or_file += "/"
        color = Fore.BLUE
    else:
        color = Fore.GREEN

    print(color + forward_cursor + name_directory_or_file + style_reset)  # Виведення імені директорії/файла


def parse_folder(path: Path, level: int = 0):
    """
    Рекурсивно виводить структуру директорії у вигляді дерева.
    :param path: Абсолютний шлях до кореневої директорії
    :param level: Поточний рівень вкладеності
    """
    try:
        # Створення винятків
        if not path.exists():
            raise Exception(f"Directory {path} not found.")
        if not path.is_absolute():
            raise Exception(f"The {path} must be a absolute path")
        if path.is_file() and level == 0:
            raise Exception(f"Root {path} cannot be a file")

        if level == 0:  # Виводимо на екран кореневу директорію
            visual_print(path.name)

        for fl in path.iterdir():  # Проходимо всю директорію
            is_dir = fl.is_dir()
            visual_print(fl.name, level=level + 1, is_dir=is_dir) # Вивід назви директорії/файлу
            if is_dir:
                parse_folder(path=fl, level=level + 1) # Якщо директорія - рекурсивно викликати
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