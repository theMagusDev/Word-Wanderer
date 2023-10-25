from ProgramFiles.working_with_data import get_user_data
from ProgramFiles.working_with_data import get_settings

def show_words():
    dictionaryList = get_user_data()["dictionary"]
    user_settings = get_settings()
    i = 0
    user_input_in_show_mode = ""

    if len(dictionaryList) == 0: # проверка на пустоту словаря
        print("Nothing to show yet. Add some words to see them.")
        return
    
    if len(dictionaryList) < user_settings["show_words_per_time"]:
        for j in range(len(dictionaryList)):
            print(dictionaryList[j]["word"], dictionaryList[j]["meaning"])
        print("You've printed the last words, your dictionary is over!")
        return # printed first and actually last words
    while user_input_in_show_mode.lower() not in ["/home", "/exit"]:
        if i + user_settings["show_words_per_time"] < len(dictionaryList):
            print("Printing next words. Enter '/home' to exit this mode.")
            for j in range(i, i + user_settings["show_words_per_time"]):
                print(dictionaryList[j]["word"], dictionaryList[j]["meaning"])
            i += user_settings["show_words_per_time"]
            print("Enter anything to continue printing or '/home' to to get to the main menu:")
            user_input_in_show_mode = input()
        else:
            print("Printing the last words.")
            for j in range(i, len(dictionaryList)):
                print(dictionaryList[j]["word"], dictionaryList[j]["meaning"])
            print("You've printed the last words, your dictionary is over!")
            return # printed last words
    if user_input_in_show_mode.lower() == '/exit':
        exit()
