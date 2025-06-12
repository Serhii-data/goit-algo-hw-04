
def parse_input(user_input) -> tuple:
    """
    Функція, яка приймає рядок вводу від користувача та розбиває її на слова: перше слово як команду, інші — як аргументи
    :param user_input: Вхідний рядок вводу від користувача
    :return: cmd - рядок - команда
            *argv - список аргументів
    """
    cmd, *argv = user_input.strip().lower().split()
    return cmd, *argv


def add_contact(contacts: dict, argv) -> str:
    """
    Функція, яка додає контакт з телефоном в словник контактів
    :param contacts: словник з контактами
    :param argv: список аргументів: ім'я контакту та телефон
    :return:
    """
    # Перевіряємо на коректність аргументів
    if len(argv) == 2:
        name, phone_number = argv
        contacts[name] = phone_number
        return "Contact added."
    return "Incorrect arguments."


def change_contact(contacts: dict, argv) -> str:
    """
   Функція, яка змінює контакт з телефоном в словнику контактів, якщо контакт відсутній - повідомлення про помилку
   :param contacts: словник з контактами
   :param argv: список аргументів: ім'я контакту та телефон
   :return:
   """
    if len(argv) == 2:
        name, phone_number = argv
        # Перевіримо чи існує контакт
        if name in contacts:
            contacts[name] = phone_number
            return "Contact updated."
        return f"{name} does not exist."
    return "Incorrect arguments."


def show_phone(contacts: dict, argv) -> str:
    """
    Функція, яка відображає номер телефону вказаного контакту, якщо контакт відсутній - повідомлення про помилку
   :param contacts: словник з контактами
   :param argv: список аргументів: ім'я контакту
   :return:
   """

    if len(argv) == 1:
        name = argv[0]
        if name in contacts:
            return f"Phone number: {contacts[name]}"
        return f"{name} does not exist."
    return "Incorrect arguments."


def show_all(contacts: dict, argv) -> str:
    """
   Функція, яка відображає весь словник контактів
   :param contacts: словник з контактами
   :param argv: список аргументів: без аргументів
   :return:
   """

    if not argv:
        header = "{:<12}: {:<12}\n".format('Name', 'Phone number')
        contacts_list = '\n'.join(["{:<12}: {:<12}".format(name, phone_number) for name, phone_number in contacts.items()])
        return header + contacts_list
    return "Incorrect arguments."


def main():

    # Словник з командами-функціями
    fun_dict = {
        'add': add_contact,
        'change': change_contact,
        'phone': show_phone,
        'all': show_all
    }
    contacts = {}
    print("Welcome to the assistant bot!")
    while True: #
        user_input = input('Enter a command: ')
        command, *argv = parse_input(user_input)
        match command:
            case 'exit' | 'close':
                print("Good bye!")
                break # вихід
            case 'hello':
                print("How can I help you?")
                continue
            case 'add' | 'change' | 'phone' | 'all': #
                print(fun_dict[command](contacts, argv))
            case _:
                print("Invalid command!")


if __name__ == '__main__':
    main()