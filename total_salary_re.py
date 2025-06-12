import re


def total_salary(path: str) -> tuple:
    """
    Функція рахує середню зарплату співробітників з текстового файлу
    :param path: шлях до текстового файлу
    :return: Повертає кортеж з двох чисел: загальної суми зарплат та середньої зарплати
    """
    total_sum_salary, average_salary = (0, 0)
    try:
        pattern = r'\d+\.\d*|\d+'
        with open(path, mode='r', encoding='utf-8') as file:
            salary_string = re.findall(pattern, file.read())
        # Формуємо список всіх зарплат
        salary = [float(developer_salary) for developer_salary in salary_string]
        total_sum_salary = sum(salary)
        average_salary = total_sum_salary / len(salary)
    # Оброблюємо винятки
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
