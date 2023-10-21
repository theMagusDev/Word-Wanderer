from working_with_data import get_dictionary

def show_words():
    dictionary = {"dictionary": get_dictionary()["dictionary"]}
    dictionaryList = dictionary["dictionary"]
    print(dictionaryList)
    i = 0
    user_input_in_show_mode = ""

    if len(dictionaryList) < 10:
        for j in range(len(dictionaryList)):
            print(dictionaryList[j]["word"], dictionaryList[j]["meaning"])
    while user_input_in_show_mode.lower() != "/home":
        if i + 10 < len(dictionaryList):
            print("Printing next 10 words. Enter '/home' to exit this mode.")
            for j in range(i, i + 10):
                print(dictionaryList[j]["word"], dictionaryList[j]["meaning"])
            i += 10
            print("Enter anything to continue printing or '/home' to to get to the main menu:")
            user_input_in_show_mode = input()
        else:
            print("Printing last words. Enter '/home' to exit this mode.")
            for j in range(i, len(dictionaryList)):
                print(dictionaryList[j]["word"], dictionaryList[j]["meaning"])
            return

    return
