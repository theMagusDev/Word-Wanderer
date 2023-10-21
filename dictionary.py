dictionary = {}
def get_dictionary():
    return dictionary

def save_dictionary(changes):
    global dictionary  # объявляем, что будем использовать глобальный словарь
    dictionary.update(changes)  # обновляем словарь с переданными изменениями

def proverka(slovo):
    for char in slovo:
        if not char.isalpha() and char != "-" and char != ' ':
            return False
    return True

def probel(slovo):
    return slovo.strip()


slovar = get_dictionary()
spisok = {}
print('At this point, you can make your own word lists\n'
        'If you want to finalize the lists,\n'
        'write "/back" in the "Enter a word in English:" field.\n')
while True:
    print('Enter a word in English:')
    slovo = probel(input())
    if slovo == '/back':
        break
    while proverka(slovo) == False:
        print("Incorrect word entered, please enter the correct word:")
        slovo = probel(input())
        if slovo == '/back':
            exit()
    print("Enter a translation of this word:")

    perevod = probel(input())
    while proverka(perevod) == False:
        print("Incorrect word entered, please enter the correct word:")
        perevod = probel(input())
    print(f'You typed the word: "{slovo}" "{perevod}" right? If yes, write "YES", if no, write "NO"')

    if probel(input()).upper() == 'YES':
        spisok = {"word": slovo, "meaning": perevod, "rating": 0}
        slovar[slovo] = spisok
        print('Your word has been successfully added!')
    else:
        print('Your word has not been added ;(\nEnter again')
        continue

save_dictionary(slovar)
