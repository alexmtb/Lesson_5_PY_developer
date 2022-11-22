#  импорт модулей с функциями, викториной, банковским счетом
import functions
import victory_3
import bank_account_3


# запуск меню только из главного модуля
if __name__ == '__main__':
    # цикл с отображением меню менеджера
    while True:
        print('1. Создать папку')
        print('2. Удалить (файл/папку)')
        print('3. Копировать (файл/папку)')
        print('4. Просмотр содержимого рабочей директории')
        print('5. Просмотреть только папки')
        print('6. Просмотреть только файлы')
        print('7. Просмотр информации об операционной системе')
        print('8. Создатель программы')
        print('9. Играть в викторину')
        print('10. Мой банковский счет')
        print('11. Смена рабочей директории')
        print('12. Выход')

        # выбираем пункт меню
        choice = input('\nВыберите пункт меню: ')

        # считываем выбор пользователя
        if choice == '1':
            functions.create_folder()
        if choice == '2':
            functions.delete_folder()
        if choice == '3':
            functions.copy_file_or_folder()
        if choice == '4':
            functions.show_directory()
        if choice == '5':
            functions.show_folders()
        if choice == '6':
            functions.show_files()
        if choice == '7':
            functions.system_info()
        if choice == '8':
            functions.author_info()
        if choice == '9':
            victory_3.victory()
        if choice == '10':
            bank_account_3.bank_account()
        if choice == '11':  # смена директории
            functions.change_dir()
        if choice == '12':
            print('Выход из программы')
            break
