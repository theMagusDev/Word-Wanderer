import sys, os, shutil
from word_add import *
from test import *
from settings import *
from words_show import *
from words_delete import *

# создание папки с данными
try: 
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(parent_dir, 'data')
    os.mkdir(path)
except OSError:
    pass

# инициализация дефолтных данных
data_exists = os.path.exists('data/data.json')
settings_exists = os.path.exists('data/settings.json')
if not data_exists:
    shutil.copy2('defaults/data.json', 'data')

if not settings_exists:
    shutil.copy2('defaults/settings.json', 'data')

#
def set_defaults():
    shutil.copy2('defaults/data.json', 'data')
    shutil.copy2('defaults/settings.json', 'data')

# функции main программы
def print_main_menu_info():
    print("Вы в главном меню. Введите:")
    print("1 для перехода в режим добавления слова; ")
    print("2 для перехода в режим тестирования; ")
    print("3 для перехода в настройки; ")
    print("4 для вывода слов; ")
    print("5 для перехода в режим удаления слов; ")
    print("/exit для завершения работы программы. ")

print("*** Language learning ***") 
print_main_menu_info()
user_input = input() 
while user_input != "/exit":
    while user_input not in "12345" and user_input != "/exit":
        print("Ошибка: введите корректную команду")
        user_input = input()
    if user_input == "/exit":
        exit()
    elif user_input == "1":
        word_add_mode()
    elif user_input == "2":
        test_mode()
    elif user_input == "3":
        settings_setup_mode()
    elif user_input == "4":
        show_words()
    elif user_input == "5":
        delete_words()
    else:
        sys.exit("Incorrect input exception")
    print_main_menu_info()
    user_input = input()
    
