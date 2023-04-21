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

def delete_contact(name):
    data = open('file.txt', 'r', encoding='utf-8')
    new_list = list()
    for line in data:
        if name.upper() not in line.upper():
            new_list.append(line)
    data.close()

    data = open('file.txt', 'w', encoding='utf-8')
    for line in new_list:
        data.writelines(line)
    data.close()

def change_contact(element, before, after):
    data = open('file.txt', 'r', encoding='utf-8')
    match element:
            case '1':
                i = 0
                j = 15
            case '2':
                i = 16
                j = 36
            case '3':
                i = 37
                j = 49
    new_list = list()
    for line in data:
        if before.upper() not in line[i:j].upper():
            new_list.append(line)
        else:
            new_list.append(line[:i] + after.ljust(j-i) + line[j:])            
    data.close()

    data = open('file.txt', 'w', encoding='utf-8')
    for line in new_list:
        data.writelines(line)
    data.close()    

def show_list():
    data = open('file.txt', 'r', encoding='utf-8')
    num = 1
    for line in data:
        print(num, line)
        num += 1
    data.close()