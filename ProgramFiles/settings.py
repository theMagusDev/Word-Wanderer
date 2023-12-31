from ProgramFiles.working_with_data import get_settings
from ProgramFiles.working_with_data import save_settings
from ProgramFiles.working_with_data import get_user_data

def print_current_settings(current_settings):
    print("Your settings:")
    print(" 1. Dictionary capacity:", current_settings["dictionary_capacity"])
    print(" 2. How many words to show in learning mode per time:", current_settings["show_words_per_time"])

def print_settings_commands():
    print("Enter '/edit' to edit some setting;")
    print("Enter '/setDefault' to reset your settings to default;")
    print("Enter '/home' to return to the main menu.")

def settings_setup_mode():
    user_input_in_settings_mode = ""
    
    while user_input_in_settings_mode != "/home":
        
        # получаем настройки пользователя
        user_settings = get_settings()

        # получаем актуальный размер словаря пользователя
        user_dict_size = len(get_user_data()["dictionary"])

        # выводим настройки и команды
        print_current_settings(user_settings)
        print_settings_commands()

        # пользователь вводит, что он хочет
        user_input_in_settings_mode = input().lower().strip() 
        while user_input_in_settings_mode not in ["/edit", "/setdefault", "/home"]:
            print("Incorrect input. Enter one of the command below:")
            print_settings_commands()
            user_input_in_settings_mode = input().lower().strip() 
        if user_input_in_settings_mode == "/edit":

            # edit mode
            print("Enter the setting index (1 or 2) you want to edit or '/cancel' to cancel editing:")
            setting_number_to_change = input().lower().strip() 
            while setting_number_to_change not in ["1", "2", "/cancel", "/home"]:
                print("Incorrect setting index or command!")
                print("Enter the setting index (1 or 2) you want to edit or '/cancel' to cancel editing:")
                setting_number_to_change = input().lower().strip() 
            
            if setting_number_to_change == "/cancel":
                print("Changes were cancelled.")
                continue
            elif setting_number_to_change == "1":
                print("Enter a new dictionary capacity:")
                new_dictionary_capacity = input().lower().strip() 
                while new_dictionary_capacity.isdigit() == False and new_dictionary_capacity != "/home" or '-' in new_dictionary_capacity or int(new_dictionary_capacity) < user_dict_size:
                    print("Incorrect value for a new dictionary capacity. Enter a positive number, not less than the number of words you have (" + str(user_dict_size) + ").")
                    print("Enter a new dictionary capacity:")
                    new_dictionary_capacity = input().lower().strip()
                if new_dictionary_capacity == "/home":
                    return
                user_settings["dictionary_capacity"] = int(new_dictionary_capacity)
                save_settings(user_settings)
                print("Saved your new settings. ")
            elif setting_number_to_change == "2":
                print("Enter a new amount of words to show in learning mode per time:")
                new_show_words_per_time = input().lower().strip()
                while new_show_words_per_time.isdigit() == False and new_show_words_per_time != "/home":
                    print("Incorrect value for an amount of words to show in learning mode per time. Enter a number.")
                    print("Enter a new amount of words to show in learning mode per time:")
                    new_show_words_per_time = input().lower().strip()
                if new_show_words_per_time == "/home":
                    return
                user_settings["show_words_per_time"] = int(new_show_words_per_time)
                save_settings(user_settings)
                print("Saved your new settings. ")
            else:
                quit("Incorrect input exception")
            
                
        elif user_input_in_settings_mode == "/setdefault":

            # set default settings mode
            user_settings["dictionary_capacity"] = 100000
            user_settings["show_words_per_time"] = 10
            save_settings(user_settings)
            print("Your settings have been reset to default.")
        elif user_input_in_settings_mode == "/home":

            # return to home
            return
        else:
            quit("Incorrect input exception")
