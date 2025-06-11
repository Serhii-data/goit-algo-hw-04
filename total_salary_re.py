import re


def total_salary(path: str) -> tuple:
    """
    Функція рахує середню зарплату співробітників з текстового файлу
    :param path: шлях до текстового файлу
    :return: Повертає кортеж з двох чисел: загальної суми зарплат та середньої зарплати
    """
    total_sum_salary, average_salary = (0, 0) # Присвоюємо початкові значення змінним
    try:
        pattern = r'\d+'
        with open(path, mode='r', encoding='utf-8') as file: # Відкриваємо текстовий файл в режимі читання
            salary_string = re.findall(pattern, file.read()) # Зчитуємо інформацію з файлу та знаходимо всі числові дані у файлі
    except FileNotFoundError: # Оброблюємо помилку на відсутність вказаного файла
        print(f"The file {path} not found.")
    except UnicodeDecodeError: # Оброблюємо помилку на невідповідність кодування
        print(f"The file {path} does not match the UTF-8 encoding.")
    else:
        salary = [int(developer_salary) for developer_salary in salary_string]  # Конвертуємо зарплату в текстовому вигляді в число
        total_sum_salary = sum(salary)  # Сума зарплат розробників
        average_salary = int(total_sum_salary / len(salary))  # Середня зарплатня розробників
    finally:
        return total_sum_salary, average_salary # Повертаємо значення


if __name__ == '__main__':

    total, average = total_salary("salary.txt")
    print(f"Total salary amount: {total}, Average salary: {average}")
