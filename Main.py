import sys
from word_add import *
from test import *
from settings import *
from words_show import *

# функции main программы
def print_main_menu_info():
    print("Вы в главном меню. Введите:")
    print("1 для перехода в режим добавления слова; ")
    print("2 для перехода в режим тестирования; ")
    print("3 для перехода в настройки; ")
    print("4 для вывода слов; ")
    print("/exit для завершения работы программы. ")

print("*** Language learning ***") 
print_main_menu_info()
user_input = input() 
while user_input != "/exit":
    while user_input not in "1234" and user_input != "/exit":
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
    else:
        sys.exit("Incorrect input exception")
    print_main_menu_info()
    user_input = input()
    
