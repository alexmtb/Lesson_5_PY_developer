import os  # импорт модуля для работы с файловой системой
import sys
import shutil  # модуль для копирования файлов


# создание папки
def create_folder():
    # запросим имя папки для создания и создадим ее, если она не существует
    folder_name = input('Назовите папку: ')
    if not os.path.isdir(f"{folder_name}"):
        os.mkdir(f"{folder_name}")
    else:
        print('\nТакая папка уже есть!\n')


# удаление папки, которую укажет пользователь
def delete_folder():
    folder_name = input('Какую папку удалить?: ')
    if os.path.exists(f"{folder_name}"):
        os.rmdir(f"{folder_name}")
        print('\nПапка удалена!\n')
    else:
        print('\nТакой папки здесь нет!\n')


# копирование папки, которую укажет пользователь
def copy_file_or_folder():
    copy_name = input('Что будем копировать? ')
    shutil.copytree(copy_name, f'{copy_name}_копия')


# содержимое текущей папки
def show_directory():
    print()
    for content in os.listdir(os.curdir):
        print(content)


# показать только папки в текущей директории
def show_folders():
    print('\nСписок папок в текущей директории:')
    for item in os.scandir(os.getcwd()):
        # если элемент - файл - выводим его на экран
        if item.is_dir():
            print(item.name)
    print()


# 6. показать только файлы в текущей директории
def show_files():
    # использование метода scandir() для получения списка файлов
    print('\nСписок файлов в текущей директории:')
    # цикл по всему содержимому каталога
    for item in os.scandir(os.getcwd()):
        # если элемент - файл - выводим его на экран
        if item.is_file():
            print(item.name)
    print()


# 7. вывод информации о системе
def system_info():
    print('Системная информация:')
    print('Используемая система:', sys.platform, '\n')
    # вывод каталогов, которые используются библиотеками, интерпретатором
    print('Каталоги, используемые интерпретатором:')
    for item in sys.path:
        print(' ', item)


# 8. Информация о создателе программы
def author_info():
    print('Автор этого кода:\nСмирнов Александр, студент Университета ИИ')


# 11. Смена рабочей папки
def change_dir():
    print(f'\nВы находитесь в каталоге:\n{os.getcwd()}')
    show_folders()
    os.chdir(input('В какой каталог перейдем?\n'))
    print(f'\nВы находитесь в каталоге:\n{os.getcwd()}')
