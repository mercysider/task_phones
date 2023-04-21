import menu, operations

def main_func():
    flag = True
    while flag: 
        user_enter = menu.user_enter()
        match user_enter:
            case '1':
                operations.add_contact(menu.add())
            case '2':
                operations.search_contact(menu.search())
            case '3':
                a, b, c = menu.change()
                operations.change_contact(a, b, c)
            case '4':
                operations.delete_contact(menu.search())
            case '5':
                operations.show_list()
            case _:
                flag = False

main_func()