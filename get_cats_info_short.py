
def get_cats_info(path: str):

    try:
        with open(path, mode='r', encoding='utf-8') as file: # Відкриття файлу по шляху path
            return [{key: value if key != 'age' else int(value) for key, value in zip(["id", "name", "age"], line.strip().split(","))}
                    for line in file.readlines()] # Формуємо список словників: проходимо одночасно по ключах та даних з файлу та додатково перетворюємо значення для "age" у число
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