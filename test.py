from working_with_data import get_dictionary
from Main import *
from time import *
import random


def check_input(string):  # проверка формата слова
    help_list = ['/help', '/home', '/exit', '/skip', '/tip', '/continue']
    if string in help_list:
        return True
    for char in range(len(string)):
        if not(string[char].isalpha()) and string[char] != '-' and string[char] != ' ':
            return False
    return True


def help_mode():  # работа со списком команд
    print("Список доступных команд:\n"
          "/help - вывод списка доступных команд\n"
          "/home - переход в главное меню\n"
          "/exit - выход из всей программы\n"
          "/skip - пропуск слова, засчитывает как неверное\n"
          "/tip - подсказка\n"
          "/continue - чтобы продолжить тестирование")
    next_string = input("Введите команду из списка: \n>> ")
    while next_string not in ['/help', '/home', '/exit', '/skip', '/tip', '/continue']:
        print("Неверный формат ввода. Введите команду из списка:")
        next_string = input('>> ')
    return next_string


def work_with_dic(tek_dic):  # работа со вводом
    cur_word = input(f"{tek_dic['meaning']} - ")
    while not(check_input(cur_word)):
        print("Неверный формат ввода. Пожалуйста, вводите только символы английского алфавита")
        cur_word = input(f"{tek_dic['meaning']} - ")
    while cur_word == '/help':
        cur_word = help_mode()
    if cur_word == '/home':
        tmp_string = input("Вы уверены, что хотите досрочно завершить тест? Вы будете перенаправлены "
                           "в главное меню. Введите: y - да, n - нет \n>> ")
        while not (tmp_string == 'y' or tmp_string == 'n'):
            print("Неверный формат ввода. Введите: y - да, n - нет")
            tmp_string = input('>> ')
        if tmp_string == 'y':
            print_main_menu_info()
            return '-1'
        elif tmp_string == 'n':
            return work_with_dic(tek_dic)
    elif cur_word == '/exit':
        tmp_string = input("Вы уверены, что хотите выйти из программы? Прогресс теста "
                           "не сохранится. Введите: y - да, n - нет \n>> ")
        while not (tmp_string == 'y' or tmp_string == 'n'):
            print("Неверный формат ввода. Введите: y - да, n - нет")
            tmp_string = input('>> ')
        if tmp_string == 'y':
            exit()
        elif tmp_string == 'n':
            return work_with_dic(tek_dic)
    elif cur_word == '/continue':
        return work_with_dic(tek_dic)
    elif cur_word == '/skip':
        return '-2'
    elif cur_word == '/tip':
        return '-3'
    return cur_word


def sklonenie(n, word):  # преобразование окончания сущ при выводе времени
    words = [word+'у', word+'ы', word]
    if all((n % 10 == 1, n % 100 != 11)):
        return str(n) + ' ' + str(words[0])
    elif all((2 <= n % 10 <= 4, any((n % 100 < 10, n % 100 >= 20)))):
        return str(n) + ' ' + str(words[1])
    return str(n) + ' ' + str(words[2])


def test_mode():
    dictionary = get_dictionary()
    print("Это режим теста. Вам будет дано значение на русском, необходимо напечатать его перевод на английский")
    pos_ans = ["You got it right!", "Well done!", "That's correct!", "Good job!", "Excellent!"]
    neg_ans = ["Don't worry! You'll learn it!", "That is not correct. Keep trying!", "Wrong! Remember this one!"
               "Don't give up! You'll memorize it!"]
    not_know_ans = ["Keep in mind this word!", "Learn this one!", "Look at this translation and remember it!"]
    random.shuffle(dictionary)
    dictionary = sorted(dictionary, key=lambda x: x["rating"])
    print("Loading your amazing words...")
    # для подсчета времени
    cur_time = gmtime()
    res1 = int(strftime("%H", cur_time)) * 3600 + int(strftime("%M", cur_time)) * 60 + int(strftime("%S", cur_time))
    # начало цикла
    for elem in range(len(dictionary)):
        tek_dic = dictionary[elem]  # обращение к словарю
        cur_word = work_with_dic(tek_dic)
        if cur_word == '-1':
            return 0
        elif cur_word == '-2':
            print(not_know_ans[random.randint(0, len(not_know_ans) - 1)])
            print(f"The right answer: {tek_dic['meaning']} - {tek_dic['word']}")
            dictionary[elem]["rating"] -= 1
        elif cur_word == '-3':
            print('ura')
        elif cur_word.isalpha():
            cur_word = cur_word.lower()
            if cur_word == tek_dic['word']:
                print(pos_ans[random.randint(0, len(pos_ans) - 1)])
                dictionary[elem]["rating"] += 1
            else:
                print(neg_ans[random.randint(0, len(neg_ans) - 1)])
                print(f"The right answer: {tek_dic['meaning']} - {tek_dic['word']}")
                dictionary[elem]["rating"] -= 1
    cur_time = gmtime()
    res2 = int(strftime("%H", cur_time)) * 3600 + int(strftime("%M", cur_time)) * 60 +\
           int(strftime("%S", cur_time)) - res1
    if res2 < 60:
        print(f"Хорошая работа! Тест завершен! Вы потратили на его выполнение {sklonenie(res2, 'секунд')}.")
    else:
        print(f"Хорошая работа! Тест завершен! Вы потратили на его выполнение {sklonenie(res2//60, 'минут')}"
              f" и {sklonenie(res2%60, 'секунд')}.")
    return 0


test_mode()
