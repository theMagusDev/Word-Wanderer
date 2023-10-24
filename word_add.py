from working_with_data import get_user_data
from working_with_data import set_user_data

def check(word):
    if len(word) == 0:
        return False
    for char in word:
        if not char.isalpha() and char not in "- ":
            return False
    return True
        
def word_add_mode():
    user_data = get_user_data()
    print('At this point, you can make your own word list. \n'
            'If you want to get back to the main menu, write "/home"')
    while True:
        print('Enter a new foreign word or "/home" to get back to the main menu:')
        word = input().strip()
        while check(word) == False:
            if word == '/home':
                return
            print("Incorrect word or command entered, please enter again:")
            word = input().strip()
        print("Enter a translation of this word:")

        translation = input().strip()
        while check(translation) == False:
            if translation == '/home':
                return
            print("Incorrect word entered, please enter the correct word:")
            translation = input().strip()
            
        print(f'You typed the word: "{word}" and its meaning "{translation}" right? If yes, write "y", if no, write "n"')
        command_to_save = input().strip().lower()
        while command_to_save not in ['y', 'n']:
            if command_to_save == '/home':
                return
            print('Incorrect answer or command! Write "y" for yes or "n" for no and "/home" to get back to the main menu:')
            command_to_save = input().strip().lower()
        if command_to_save == 'y':
            user_data["dictionary"].append({"word": word.lower(), "meaning": translation, "rating": 0})
            set_user_data(user_data)
            print('Your word has been successfully added!')
        else:
            print('Ok, this word has not been added. ')
            continue
