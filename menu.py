def user_enter():
    print("- Добавить контакт: введите 1")
    print("- Найти контакт: введите 2")
    print("- Изменить контакт: введите 3")
    print("- Удалить: введите 4")
    print("- Просмотр справочника: введите 5")
    print("- Выйти: введите 0")
    ue = input("Выберите пункт меню: ")
    return ue

def add():
    firstname = input("Введите имя: ")
    secondname = input("Введите фамилию: ")
    phone = input("Введите номер: ")
    return firstname.ljust(15) + ' ' + secondname.ljust(20) + ' ' + phone.ljust(12)

def search():
    name = input("Введите имя или фамилию: ")
    return name

def change():
    print("Что вы хотите изменить?")
    print("Имя: введите 1")
    print("Фамилию: введите 2")
    print("Телефон: введите 3")
    element = input("Введите пункт меню: ")
    before = input("Введите изменяемое значение: ")
    after = input("Введите новое значение: ")
    return element, before, after
    



