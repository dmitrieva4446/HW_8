'''Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной'''


'''Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
Пользователь также может ввести имя или фамилию, и Вы должны реализовать 
функционал для изменения и удаления данных.'''


from os.path import exists
from csv import DictReader, DictWriter


def check_phone(num):
    flag = False
    phone_number = int(num)
    while not flag:
        try:
            if len(str(phone_number)) != 11:
                phone_number = int(input("Неверный номер.\nВведите корректный номер телефона: "))
            else:
                flag = True
        except ValueError:
            print('not valid number')
    return phone_number


def get_info():
    info = []
    first_name = input("Введите фамилию: ")
    last_name = input("Введите имя: ")
    info.append(first_name)
    info.append(last_name)
    info.append(check_phone(input("Введите номер телефона: ")))
    return info


def create_file():
    with open('phone.csv', 'w', encoding='utf-8', newline='') as data:
        f_n_writer = DictWriter(data, fieldnames=['id', 'Фамилия', 'Имя', 'Номер'])
        f_n_writer.writeheader()


def write_file(lst):
    with open('phone.csv', 'r', encoding='utf-8', newline='') as f_n:
        f_n_reader = DictReader(f_n)
        res = list(f_n_reader)
    with open('phone.csv', 'w', encoding='utf-8', newline = '') as f_n:
        obj = {'id': len(res), 'Фамилия': lst[0], 'Имя': lst[1], 'Номер': lst[2]}
        res.append(obj)
        f_n_writer = DictWriter(f_n, fieldnames=['id', 'Фамилия', 'Имя', 'Номер'])
        f_n_writer.writeheader()
        f_n_writer.writerows(res)


def read_file(file_name):
    with open(file_name, encoding='utf-8') as f_n:
        f_n_reader = DictReader(f_n)
        phone_book = list(f_n_reader)
    return phone_book


def print_info():
    phone_book = read_file('phone.csv')
    ret = 'id Фамилия Имя Номер\n'
    for row in phone_book:
        ret += row['id']+' '+row['Фамилия']+' '+ row['Имя']+' '+ row['Номер']+'\n'
    return ret


def record_info():
    lst = get_info()
    write_file(lst)


def edit_info():
    print(print_info())
    sel_id = int(input("Укажите id записи для редактирования: "))
    phone_book = read_file('phone.csv')
    if(0 <= sel_id < len(phone_book)):
        row = phone_book[sel_id]
        first_name = input("Введите фамилию: ")
        last_name = input("Введите имя: ")
        phone_num = check_phone(input("Введите номер телефона: "))
        row = {'id': sel_id, 'Фамилия': first_name, 'Имя': last_name, 'Номер': phone_num}
        with open('phone.csv', 'w', encoding='utf-8', newline='') as f_n:
            phone_book[sel_id] = row
            f_n_writer = DictWriter(f_n, fieldnames=['id', 'Фамилия', 'Имя', 'Номер'])
            f_n_writer.writeheader()
            f_n_writer.writerows(phone_book)
    else:
        print("Ошибка! Введен несуществующий id")


def delete_info():
    print(print_info())
    sel_id = int(input("Укажите id записи для УДАЛЕНИЯ: "))
    phone_book = read_file('phone.csv')
    if(0 <= sel_id < len(phone_book)):
        del(phone_book[sel_id])
        for i in range(len(phone_book)):
            row = phone_book[i]
            row['id'] = i
            phone_book[i] = row
        with open('phone.csv', 'w', encoding='utf-8', newline='') as f_n:
            f_n_writer = DictWriter(f_n, fieldnames=['id', 'Фамилия', 'Имя', 'Номер'])
            f_n_writer.writeheader()
            f_n_writer.writerows(phone_book)


def main():
    while True:
        command = input('\n r -вывод данных\n w -записать данные\n e -редактировать\n d -удалить\n q -выход\n\nВведите команду: ')
        print()
        if command == 'q':
            break
        elif command == 'r':
            if not exists('phone.csv'):
                print('Файл не создан')
                break
            print(print_info())
        elif command == 'w':
            if not exists('phone.csv'):
                create_file()
                record_info()
            else:
                record_info()
        elif command == 'e':
            if not exists('phone.csv'):
                print('Файл не создан')
            else:
                edit_info()
        elif command == 'd':
            if not exists('phone.csv'):
                print('Файл не создан')
            else:
                delete_info()


main()