import sys, os, shutil
from ProgramFiles.word_add import *
from ProgramFiles.test import *
from ProgramFiles.settings import *
from ProgramFiles.words_show import *
from ProgramFiles.words_delete import *
from ProgramFiles.working_with_data import get_user_data

initialize_data()

# функции main программы
def get_user_status(score):
    if score < 50:
        return "Starter"
    elif score < 150:
        return "Glottologist"
    elif score < 500:
        return "Polyglot"
    elif score < 1500:
        return "Philologist"
    else:
        return "Word-nerd"
    

def print_main_menu_info():
    user_data = get_user_data()
    print("Вы в главном меню. Ваш статус:", get_user_status(user_data["score"]))
    print("Введите:")
    print("1 для перехода в режим добавления слова; ")
    print("2 для перехода в режим тестирования; ")
    print("3 для перехода в настройки; ")
    print("4 для вывода слов; ")
    print("5 для перехода в режим удаления слов; ")
    print("/exit для завершения работы программы. ")

print("*** Language learning ***") 
print_main_menu_info()
user_input = input().lower().strip() 
while user_input != "/exit":
    while user_input not in "12345" and user_input != "/exit":
        print("Ошибка: введите корректную команду")
        user_input = input().lower().strip() 
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
    user_input = input().lower().strip() 
    
