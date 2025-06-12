
def get_cats_info(path: str):

    try:
        with open(path, mode='r', encoding='utf-8') as file:
            # Формуємо список словників: проходимо одночасно по ключах та даних з файлу
            return [{key: value for key, value in zip(["id", "name", "age"], line.strip().split(","))}
                    for line in file.readlines()]
    # Обробка винятків
    except FileNotFoundError:
        print(f"The file {path} not found.")
        return None
    except PermissionError:
        print(f"No access rights to the file {path}")
        return None


if __name__ == "__main__":
    cats_info = get_cats_info("cats_file.txt")
    if cats_info:
        print(cats_info)