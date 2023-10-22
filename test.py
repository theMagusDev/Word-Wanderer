from working_with_data import *
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
    print("List of available commands:\n"
          "/help - list of available commands\n"
          "/home - switch to the main menu\n"
          "/exit - exit from the entire program\n"
          "/skip - omission of a word, counts as an incorrect word\n"
          "/tip - hint\n"
          "/continue - to continue testing")
    next_string = input("Enter a command from the list: \n>> ").strip()
    while next_string not in ['/help', '/home', '/exit', '/skip', '/tip', '/continue']:
        print("Invalid input format. Enter a command from the list:")
        next_string = input('>> ').strip()
    return next_string


def work_with_dic(tek_dic):  # работа со вводом
    cur_word = input(f"{tek_dic['meaning']} - ").strip()
    while not(check_input(cur_word)):
        print("Invalid input format. Please enter English alphabet characters only.")
        cur_word = input(f"{tek_dic['meaning']} - ").strip()
    while cur_word == '/help':
        cur_word = help_mode()
    if cur_word == '/home':
        tmp_string = input("Are you sure you want to complete the test early? "
                           "You will be redirected to the main menu. Enter: y - yes, n - no \n>> ").strip()
        while not (tmp_string == 'y' or tmp_string == 'n'):
            print("Invalid input format. Enter: y - yes, n - no")
            tmp_string = input('>> ').strip()
        if tmp_string == 'y':
            return '-1'
        elif tmp_string == 'n':
            return work_with_dic(tek_dic)
    elif cur_word == '/exit':
        tmp_string = input("Are you sure you want to exit the program? "
                           "The test progress will not be saved. Enter: y - yes, n - no \n>> ").strip()
        while not (tmp_string == 'y' or tmp_string == 'n'):
            print("Invalid input format. Enter: y - yes, n - no")
            tmp_string = input('>> ').strip()
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


def time_moment(res2, string):
    if res2 == 1:
        return str(res2) + ' ' + string
    return str(res2) + ' ' + string+'s'


def int_r(num):
    num = int(num + (0.5 if num > 0 else -0.5))
    return num


def hint(tek_dic, num):
    ans = tek_dic["word"]
    len_word = len(ans)
    if num == 1:
        if len_word <= 5:
            print(f"{tek_dic['meaning']} - {ans[:1]}")
        else:
            print(f"{tek_dic['meaning']} - {ans[:int_r(len_word*0.25)]}")
    else:
        if len_word <= 5:
            print(f"{tek_dic['meaning']} - {ans[:2]}")
        else:
            print(f"{tek_dic['meaning']} - {ans[:int_r(len_word*0.25)*2]}")


def word_with_answers(cur_word, tek_dic):
    len_word = len(tek_dic["word"])
    ctip = 0
    while ctip <= 2:
        if cur_word == "-3" and ctip != 2:
            if len_word == 1:
                return "sc-1"
            elif len_word == 2 and ctip == 1:
                return "sc-2"
            ctip += 1
            hint(tek_dic, ctip)
        else:
            cur_word = cur_word.lower()
            if cur_word == tek_dic['word']:
                if ctip == 0:
                    return "sc2"
                elif ctip == 1:
                    return "sc1"
                else:
                    return "sc0"
            else:
                return "sc-1"
        cur_word = work_with_dic(tek_dic)
    return "sc-1"


def test_mode():
    dictionary = get_user_data()["dictionary"]
    if len(dictionary) == 0:
        print("Oups! The dictionary is empty! Nothing to check! Add new words and let's get started! ")
        return 0
    print("This is a test mode. You will be given a value in one language, "
          "you need to type its translation into English. If you want to close test_mode "
          "enter: /home")
    pos_ans = ["You got it right!", "Well done!", "That's correct!", "Good job!", "Excellent!"]
    neg_ans = ["Don't worry! You'll learn it!", "That is not correct. Keep trying!", "Wrong! Remember this one!"
               "Don't give up! You'll memorize it!"]
    not_know_ans = ["Keep in mind this word!", "Learn this one!", "Look at this translation and remember it!"]
    random.shuffle(dictionary)
    dictionary = sorted(dictionary, key=lambda x: x["rating"])
    count, count_ob = 0, 0
    res_for_score, bonus_score = 0, 0
    print("Loading your amazing words...")
    # для подсчета времени
    cur_time = gmtime()
    res1 = int(strftime("%H", cur_time)) * 3600 + int(strftime("%M", cur_time)) * 60 + int(strftime("%S", cur_time))
    # начало цикла
    for elem in range(len(dictionary)):
        tek_dic = dictionary[elem]  # обращение к словарю
        cur_word = work_with_dic(tek_dic)
        if cur_word == '-1':
            cur_time = gmtime()
            res2 = int(strftime("%H", cur_time)) * 3600 + int(strftime("%M", cur_time)) * 60 + \
                int(strftime("%S", cur_time))-res1
            if res2 < 60:
                print(f"Good job! The test is complete! You score is {count}/{count_ob}! "
                      f"You spent {time_moment(res2, 'second')}.")
            else:
                print(f"Good job! The test is complete! You score is {count}/{count_ob}! "
                      f"You spent {time_moment(res2 // 60, 'minute')} and {time_moment(res2 % 60, 'second')}.")
            new_data = get_user_data()
            new_data["score"] += res_for_score
            new_data["dictionary"] = dictionary
            set_user_data(new_data)
            return 0
        elif cur_word == '-2':
            count_ob += 1
            bonus_score = 0
            print(not_know_ans[random.randint(0, len(not_know_ans) - 1)])
            print(f"The right answer: {tek_dic['meaning']} - {tek_dic['word']}")
            dictionary[elem]["rating"] -= 1
        else:
            ans = word_with_answers(cur_word, tek_dic)
            if ans == "sc2":  # without tips
                count += 1
                count_ob += 1
                print(pos_ans[random.randint(0, len(pos_ans) - 1)])
                bonus_score += 1
                res_for_score += bonus_score
                dictionary[elem]["rating"] += 2
            elif ans == "sc1":  # one tip
                count += 1
                count_ob += 1
                bonus_score = 0
                res_for_score += 1
                print(pos_ans[random.randint(0, len(pos_ans) - 1)])
                dictionary[elem]["rating"] += 1
            elif ans == "sc0":  # two tips
                count += 1
                count_ob += 1
                bonus_score = 0
                res_for_score += 1
                print(pos_ans[random.randint(0, len(pos_ans) - 1)])
            else:
                count_ob += 1
                bonus_score = 0
                print(neg_ans[random.randint(0, len(neg_ans) - 1)])
                print(f"The right answer: {tek_dic['meaning']} - {tek_dic['word']}")
                dictionary[elem]["rating"] -= 1
    cur_time = gmtime()
    res2 = int(strftime("%H", cur_time)) * 3600 + int(strftime("%M", cur_time)) * 60 +\
        int(strftime("%S", cur_time)) - res1
    if res2 < 60:
        print(f"Good job! The test is complete! You score is {count}/{len(dictionary)}! "
              f"You spent {time_moment(res2, 'second')}.")
    else:
        print(f"Good job! The test is complete! You score is {count}/{len(dictionary)}! "
              f"You spent {time_moment(res2//60, 'minute')} and {time_moment(res2%60, 'second')}.")
    new_data = get_user_data()
    new_data["score"] += res_for_score
    new_data["dictionary"] = dictionary
    set_user_data(new_data)
    return 0
