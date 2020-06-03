import string

print('Переводчик с языка или на язык неправильной раскладки')
print('The Wrong Keyboard Layout Translator')
s = input('Введите текст/Insert your text: ')

letters_rus_uppercase = ('ЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ')
letters_rus_lowercase = ('ёйцукенгшщзхъфывапролджэячсмитьбю')
letters_eng_uppercase = ("~QWERTYUIOP{}ASDFGHJKL:'ZXCVBNM<>")
letters_eng_lowercase = ("`qwertyuiop[]asdfghjkl;'zxcvbnm,.")
result = ''

for symbol in s:

    if symbol in letters_rus_uppercase:   # RUS Upper
        num = letters_rus_uppercase.find(symbol)
        sym_opposite = letters_eng_uppercase[num]
        result += sym_opposite

    elif symbol in letters_rus_lowercase: # RUS Lower
        num = letters_rus_lowercase.find(symbol)
        sym_opposite = letters_eng_lowercase[num]
        result += sym_opposite

    elif symbol in letters_eng_lowercase: # ENG Lower
        num = letters_eng_lowercase.find(symbol)
        sym_opposite = letters_rus_lowercase[num]
        result += sym_opposite

    elif symbol in letters_eng_uppercase: # ENG Upper
        num = letters_eng_uppercase.find(symbol)
        sym_opposite = letters_rus_uppercase[num]
        result += sym_opposite

    else:
        result += symbol

print('Результат/Result: %s' % result)



