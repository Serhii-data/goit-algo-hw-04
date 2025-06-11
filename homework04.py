
def parse_input(user_input) -> tuple:
    """
    Функція, яка приймає рядок вводу від користувача та розбиває її на слова: перше слово як команду, інші — як аргументи
    :param user_input: Вхідний рядок вводу від користувача
    :return: cmd - рядок - команда
            *argv - список аргументів
    """
    cmd, *argv = user_input.strip().lower().split() # Обробляємо рядок вводу від користувача (видаляємо зайві пробіли, приводимо до нижнього регістру та розбиваємо на команду та список аргументів
    return cmd, *argv  # Повертаємо окремо рядок з командою та список аргументів


def add_contact(contacts: dict, argv) -> None:
    """
    Функція, яка додає контакт з телефоном в словник контактів
    :param contacts: словник з контактами
    :param argv: список аргументів: ім'я контакту та телефон
    :return:
    """
    if len(argv) == 2: # Перевіряємо на коректність аргументів
        name, phone_number = argv # Присвоюємо змінним аргументи: ім'я та номер телефону
        contacts[name] = phone_number # Добавляємо контакт та телефон до словника контактів
        print("Contact added.") # Успішне добавлення контакту
    else:
        print("Incorrect arguments") # Якщо кількість аргументів не відповідає команді


def change_contact(contacts: dict, argv) -> None:
    """
   Функція, яка змінює контакт з телефоном в словнику контактів, якщо контакт відсутній - повідомлення про помилку
   :param contacts: словник з контактами
   :param argv: список аргументів: ім'я контакту та телефон
   :return:
   """
    if len(argv) == 2: # Перевіряємо на коректність аргументів
        name, phone_number = argv # Присвоюємо змінним аргументи: ім'я та номер телефону
        if name in contacts: # Перевіряємо чи контакт існує
            contacts[name] = phone_number # Змінюємо існуючий контакт
            print("Contact updated.") # Успішне оновлення контакту
        else:
            print("The contact with this name does not exist.") # Контакт не існує
    else:
        print("Incorrect arguments") # Якщо кількість аргументів не відповідає команді


def show_phone(contacts: dict, argv) -> None:
    """
    Функція, яка відображає номер телефону вказаного контакту, якщо контакт відсутній - повідомлення про помилку
   :param contacts: словник з контактами
   :param argv: список аргументів: ім'я контакту
   :return:
   """
    if len(argv) == 1: # Перевіряємо на коректність аргументів
        name = argv[0]
        if name in contacts: # Перевіряємо чи контакт існує
            print(f"Phone number: {contacts[name]}") # Виводимо номер телефону
        else:
            print("The contact with this name does not exist.") # Контакт не існує
    else:
        print("Incorrect arguments") # Якщо кількість аргументів не відповідає команді


def show_all(contacts: dict, argv) -> None:
    """
   Функція, яка відображає весь словник контактів
   :param contacts: словник з контактами
   :param argv: список аргументів: без аргументів
   :return:
   """
    if not argv: # Перевіряємо на коректність аргументів
        print("{:<15}: {:<15}".format('Name', 'Phone number')) # Виводимо список контактів і їх номера телефонів
        for name, phone_number in contacts.items():
            print("{:<15}: {:<15}".format(name, phone_number))
    else:
        print("Incorrect arguments") # Якщо кількість аргументів не відповідає команді


def main():

    # Словник, який співставляє команди та відповідні їм методи роботи з контактами
    fun_dict = {
        'add': add_contact,
        'change': change_contact,
        'show': show_phone,
        'all': show_all
    }
    contacts = {} # Словник з контактами
    print("Welcome to the assistant bot!")
    while True: #
        user_input = input('Enter a command: ') # Запит на ввід команди від користувача
        command, *argv = parse_input(user_input)
        match command: # Оброблюємо команди користувача
            case 'exit' | 'close': # Тоді припиняємо бот
                print("Good bye!")
                break # вихід
            case 'hello':
                print("How can I help you?")
                continue
            case 'add' | 'change' | 'show' | 'all': #
                fun_dict[command](contacts, argv) # Викликаємо метод, який відповідає заданій команді
            case _:
                print("Invalid command!")


if __name__ == '__main__':
    main()