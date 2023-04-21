def user_enter():
    print("- Добавить контакт: введите 1")
    print("- Найти контакт: введите 2")
    print("- Просмотр справочника: введите 3")
    print("- Выйти: введите 0")
    ue = input("Введите пункт меню: ")
    return ue

def add():
    firstname = input("Введите имя: ")
    secondname = input("Введите фамилию: ")
    phone = input("Введите номер: ")
    return firstname.ljust(15) + ' ' + secondname.ljust(20) + ' ' + phone.ljust(15)

def search():
    name = input("Введите имя или фамилию: ")
    return name


