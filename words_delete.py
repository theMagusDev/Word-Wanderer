from working_with_data import *


def check_input_for_delete(string):  # проверка формата слова
    if string == '/home':
        return True
    for char in range(len(string)):
        if not(string[char].isalpha()) and string[char] != '-' and string[char] != ' ':
            return False
    return True


def work_with_item():  # работа со вводом
    cur_word = input("Enter word if you want to delete it or '/home' to close delete mode: ").strip()
    while not(check_input_for_delete(cur_word)):
        print("Invalid input format. Please enter English alphabet characters only.")
        cur_word = input("Enter the word in English that you want to delete: ").strip()
    if cur_word == '/home':
        tmp_string = input("Are you sure you want to exit from delete_mode? "
                           "You will be redirected to the main menu. Enter: y - yes, n - no \n>> ").strip()
        while not (tmp_string == 'y' or tmp_string == 'n'):
            print("Invalid input format. Enter: y - yes, n - no")
            tmp_string = input('>> ').strip()
        if tmp_string == 'y':
            return '-1'
        elif tmp_string == 'n':
            return work_with_item()
    return cur_word


def delete_words():
    dictionary = get_dictionary()["dictionary"]
    new_dictionary = dictionary
    print(dictionary)
    if len(dictionary) == 0:
        print("Oups! The dictionary is empty! Nothing to delete!")
        return 0
    print("You are now in delete mode. Type a word you would like to delete. If you want to close delete mode "
          "enter: /home")
    item = work_with_item()
    while item != "-1":
        while not(any(item in i["word"] for i in dictionary)):
            print("Unfortunately, there is no such word in the dictionary! Try again! ")
            item = work_with_item()
        for i in dictionary:
            if item in i["word"]:
                translation = i["meaning"]
                tmp_phrase = input(f"Found the word '{item}' with the translation '{translation}'. "
                                   f"Do you want to delete it or continue searching?\n"
                                   f"Enter: '/delword' for deleting or '/cont' to continue searching "
                                   f"without deletion this word \n>> ").strip()
                while not (tmp_phrase == '/delword' or tmp_phrase == '/cont'):
                    print("Invalid input format. Enter: /delword - for deleting, /cont - to continue searching")
                    tmp_phrase = input('>> ').strip()
                if tmp_phrase == '/delword':
                    tmp_string = input("Are you sure you want to delete this word? "
                                       "The deletion cannot be undone. Enter: y - yes, n - no \n>> ").strip()
                    while not (tmp_string == 'y' or tmp_string == 'n'):
                        print("Invalid input format. Enter: y - yes, n - no")
                        tmp_string = input('>> ').strip()
                    if tmp_string == 'y':
                        new_dictionary = [i for i in dictionary if
                                          not ((translation in i['meaning']) and (item in i['word']))]
                        print("The word was successfully deleted!")
        print("You have reached the end of the list.")
        dictionary = new_dictionary
        item = work_with_item()
    dictionary = new_dictionary
    print(dictionary)
    print("All changes are saved in the dictionary! Redirect to the main menu...")
    new_data = get_user_data()
    new_data["dictionary"] = dictionary
    set_user_data(new_data)
    return 0
