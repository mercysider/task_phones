def add_contact(contact):
    data = open('file.txt', 'a', encoding='utf-8')
    data.writelines(contact)
    data.write('\n')
    data.close()

def search_contact(name):
    data = open('file.txt', 'r', encoding='utf-8')
    count = 0
    for line in data:
        if name.upper() in line.upper():
            print(line)
            count += 1
    if count == 0:
        print('Контакты не найдены')
    else:
        print(f'Всего найдено контактов: {count}')
    data.close()

def show_list():
    data = open('file.txt', 'r', encoding='utf-8')
    num = 1
    for line in data:
        print(num, line)
        num += 1
    data.close()