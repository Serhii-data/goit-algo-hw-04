import sys


def total_salary(path: str) -> tuple:
    """
    Функція читає інформацію з файлу та повертає суму та середню зарплату розробників
    :param path: шлях до текстового файлу
    :return: Повертає кортеж з двох чисел: загальної суми зарплат та середньої зарплати
    """
    total_sum_salary, average_salary, count_developers = (0, 0, 0)
    try:
        with open(path, mode='r', encoding='utf-8') as file:
            for line in file.readlines():
                developer, developer_salary = line.split(',')
                total_sum_salary += float(developer_salary)
                count_developers += 1

        average_salary = (total_sum_salary / count_developers)
    # Обробка винятків
    except FileNotFoundError:
        print(f"The file {path} not found.")
    except UnicodeDecodeError:
        print(f"The file {path} does not match the UTF-8 encoding.")
    except ZeroDivisionError as e:
        print(e)
    finally:
        return total_sum_salary, average_salary

if __name__ == '__main__':

    total, average = total_salary("salary.txt")
    print(f"Total salary amount: {total}, Average salary: {average}")
