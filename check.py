def check_index(massage: str, len_menu: int):
    print(massage)
    while True:
        index_menu = input(f'Введите число от 1 до {len_menu}: ')
        if index_menu.isdigit() and 0 < int(index_menu) <= len_menu:
            return int(index_menu)
