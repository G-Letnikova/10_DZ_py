import phone_book
import check

pb = phone_book.PhoneBook('phone_db.txt')

while True:
    print(pb.main_menu())
    choice = check.check_index('Выберете пункт меню ', len(list(pb.main_menu().split('\n')))-1)  # + проверка

    match choice:

        case 1:
            print(pb)

        case 2:
            name = input('Введите имя: ')
            phone = input('Введите телефон: ')
            comment = input('Введите комментарий: ')
            pb.new_contact(name, phone, comment)

        case 3:
            word = input('Ввелите искомый контакт: ')
            print(pb.search(word) if pb.search(word) else f'--- контакт {word} не найден ---')  # + проверка на наличее

        case 4:
            print(pb)
            index = check.check_index('Выберете ИНДЕКС для изменения контакта: ', len(pb.phone_list))  # + проверка

            name = input('Введите ИМЯ для изменения контакта (или Enter, чтобы не менять): ')
            phone = input('Введите ТЕЛЕФОН для изменения контакта (или Enter, чтобы не менять): ')
            comment = input('Введите КОММЕНТАРИЙ для изменения контакта (или Enter, чтобы не менять): ')
            pb.change(index-1, name, phone, comment)

        case 5:
            print(pb)
            index = check.check_index('Выберете ИНДЕКС для удаления контакта: ', len(pb.phone_list))  # + проверка

            pb.delete(index-1)

        case 6:
            pb.save()

        case 7:
            break
