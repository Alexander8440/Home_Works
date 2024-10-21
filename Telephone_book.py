import os


TELEPHONE_DIRECTORY_MENY: tuple = (
    'Показать все контакты',
    'Добавить контакт',
    'Удалить контакт',
    'Редактировать контакт',
    'Найти контакт',
)

telephone_book: dict = {}

def creating_a_telephone_directory():
    """Функция создания справочника"""
    name: str = input('Введите имя: ')
    number: str = input('Введите номер: ')
    with open('text.txt','w',encoding='UTF-8') as text:
        text.write(f'{name}-{number}' )
        text.close()

def next_id(telephone_book: telephone_book):
    """Функция создания id контактов
    :type telephone_book: dict
    """
    if telephone_book:
        return max(telephone_book) + 1
    return 1


def open_directory():
    """Функция открытия текстового файла и передача его информации в переменную"""
    with open('text.txt', 'r+', encoding='UTF-8') as text:
        show_cont: list = sorted(text.readlines(), key=lambda x: x[0])
        show_cont: list = list(map(lambda x: x.strip().split('-'), show_cont))
        for contact in show_cont:
            telephone_book[next_id(telephone_book)]: dict = {'name': contact[0],
                                                       'phone': contact[1]}
        return telephone_book


def show_all_contacts():
    """Функция показа контактов"""
    for num, contact in telephone_book.items():
        print(f'{num}:{contact}')


def add_contact():
    """Функция добавления контакта"""
    name: str = input('Введите Имя: ')
    number: str = input('Введите номер: ')
    contacs: str = f'{name}-{number}'
    with open('text.txt', 'a+', encoding='UTF-8') as text:
        text.write(f'\n{contacs}')
        text.close()


def delete_contacts():
    """Функция удаления контакта"""
    for a, s in telephone_book.items():
        print(f'{a}:{s}')
    number: int = int(input('Введите номер контакта который хотите удалить: '))
    for key in telephone_book.keys():
        if key == number:
            del telephone_book[number]
            print('Контакт успешно удален')
            return telephone_book


def save_contacts():
    """Функция сохранения контакта"""
    with open('text.txt', 'w', encoding='UTF-8') as text:
        data: [list,str] = []
        for contact in telephone_book.values():
            data.append('-'.join(contact.values()))
        data = '\n'.join(data)
        text.write(data)
        text.close()


def edit_contact():
    """Функция редактирования контакта"""
    for num_id, contact in telephone_book.items():
        print(f'{num_id}:{contact}')
    num: int = int(input('Ведите номер контакта который хотите изменить: '))
    print(telephone_book[num])
    dic: dict = telephone_book[num]
    dic['name'] = input('Введите изменения в имени: ')
    dic['phone'] = input('Введите изменения в номере: ')
    telephone_book[num] = dic
    return telephone_book


def find_contacts():
    """Функция поиска контакта"""
    name: str = input('Ведите имя для поиска: ')
    for num_id, contacts in telephone_book.items():
        if name.lower() == contacts['name'].lower():
            print(contacts)


def start_program():
    """Функция начало программы"""
    print('Главное меню')
    if os.path.isfile('text.txt'):
        open_directory()
        for num, menu in enumerate(TELEPHONE_DIRECTORY_MENY, 1):
            print(f'{num}.{menu}')
        menu_selection = input('Выберите пункт меню ')
        if menu_selection == '1':
            show_all_contacts()
        elif menu_selection == '2':
            add_contact()
        elif menu_selection == '3':
            delete_contacts()
            save_contacts()
        elif menu_selection == '4':
            edit_contact()
            save_contacts()
        elif menu_selection == '5':
            find_contacts()
    else:
        print('Справочник пуст, создайте первый контакт')
        creating_a_telephone_directory()

start_program()
