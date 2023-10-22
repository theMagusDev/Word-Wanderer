from working_with_data import get_user_data
from working_with_data import set_user_data

def word_add_mode():
    def check(word, english):
        if english:
            for char in word:
                if not char in "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM- ":
                    return False
            return True
        else:
            for char in word:
                if not char.isalpha():
                    return False
            return True

    user_data = get_user_data()
    print('At this point, you can make your own word lists\n'
            'If you want to get back to the main menu,\n'
            'write "/home" in the "Enter a word in English:" field.\n')
    while True:
        print('Enter a new word in English or "/home" to get back to the main menu:')
        word = input().strip()
        if word == '/home':
            return
        while check(word, True) == False:
            print("Incorrect word entered, please enter the correct word:")
            word = input().strip()
            if word == '/back':
                exit()
        print("Enter a translation of this word:")

        translation = input().strip()
        while check(translation, False) == False:
            print("Incorrect word entered, please enter the correct word:")
            translation = input().strip()
        print(f'You typed the word: "{word}" and its meaning "{translation}" right? If yes, write "y", if no, write "n"')

        if input().strip().lower() == 'y':
            user_data["dictionary"].append({"word": word.lower(), "meaning": translation, "rating": 0})
            set_user_data(user_data)
            print('Your word has been successfully added!')
        else:
            print('Your word has not been added ;(\nEnter again')
            continue
