def word_add_mode():
    pass
def test_mode():
    pass
def settings_setup_mode():
    pass

print("*** Language learning ***")
print("Вы в главном меню. Введите:")
print("1 для перехода в режим добавления слова; ")
print("2 для перехода в режим тестирования; ")
print("3 для перехода в настройки. ")
print("/exit для завершения работы программы. ")
user_input = input()
while user_input != "/exit":
    while user_input not in "123" and user_input != "/exit":
        print("Ошибка: введите корректную команду")
        user_input = input()
    if user_input == "/exit":
        exit()
    elif user_input == "1":
        word_add_mode()
    elif user_input == "2":
        word_add_mode()
    elif user_input == "3":
        word_add_mode()
    else:
        exit("Incorrect input exception")
    
