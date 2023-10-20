from working_with_data import get_dictionary

def show_words():
    dictionary = get_dictionary()
    i = 0
    user_input_in_show_mode = ""
    
    while user_input_in_show_mode != "/back":
        print("Printing next 10 words. Enter '/back' to exit this mode.")
        for j in range(i, i + 10):
            print(dictionary[i]["word"], dictionary[i]["meaning"])
        i += 10
        user_input_in_show_mode = input()
    return
