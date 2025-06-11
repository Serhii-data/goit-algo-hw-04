import sys


def total_salary(path: str) -> tuple:
    """
    Функція читає інформацію з файлу та повертає суму та середню зарплату розробників
    :param path: шлях до текстового файлу
    :return: Повертає кортеж з двох чисел: загальної суми зарплат та середньої зарплати
    """
    total_sum_salary, average_salary, count_developers = (0, 0, 0) # Присвоюємо початкові значення змінним
    try:
        with open(path, mode='r', encoding='utf-8') as file: # Відкриваємо текстовий файл в режимі читання
            for line in file.readlines():
                developer, developer_salary = line.split(',') #Зчитуємо ім'я розробника та зарплату
                total_sum_salary += int(developer_salary) # Додаємо поточну заробітню платню до суми
                count_developers += 1 # Вираховуємо кількість розробників
    except FileNotFoundError: # Оброблюємо помилку на відсутність вказаного файла
        print(f"The file {path} not found.")
    except UnicodeDecodeError: # Оброблюємо помилку на невідповідність кодуванню
        print(f"The file {path} does not match the UTF-8 encoding.")
    else:
        average_salary = int(total_sum_salary / count_developers) # Отримуємо точне значення середньої зарплати
    finally:
        return total_sum_salary, average_salary #повертаємо загальну суму та середню зарплату розробників

if __name__ == '__main__':

    total, average = total_salary("salary.txt")
    print(f"Total salary amount: {total}, Average salary: {average}")
