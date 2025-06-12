
def get_cats_info(path: str):
    keys = ["id", "name", "age"] # Список ключів про котів
    cats_info_result = []
    try:
        with open(path, mode='r', encoding='utf-8') as file:
            for line in file.readlines(): 
                value_cat = line.strip().split(",")

                if len(value_cat) != len(keys):
                    raise ValueError("There must be 3 values")

                info_about_the_cat = {}
                for inx, value in enumerate(value_cat):
                    info_about_the_cat[keys[inx]] = value
                cats_info_result.append(info_about_the_cat)
    # Оброблюємо винятки
    except FileNotFoundError:
        print(f"The file {path} not found.")
        return None
    except PermissionError:
        print(f"No access rights to the file {path}")
        return None
    except ValueError as e:
        print(e)
        return None
    else:
        return cats_info_result


if __name__ == "__main__":
    cats_info = get_cats_info("cats_file.txt")
    if cats_info:
        print(cats_info)