#from collections import Counter
#def count_letters(text):
#    text_lower = text.lower()
#    alphabet = dict()
#    for letter in text_lower:
#        if letter.isalpha():
#            c = Counter(text_lower)
#     return (c)
def count_letters(text):
    text_lower = text.lower()
    alphabet = dict()
    for letter in text_lower:
        if letter.isalpha():
            if letter not in alphabet:
                alphabet[letter] = 1
            else:
                alphabet[letter] += 1
    return alphabet


#def calculate_frequency(alphabet_2):
#    for a, b, in alphabet_2.items():
#        alphabet_2[a] = round((alphabet_2[a]/ len(alphabet_2)),2)
#    return alphabet_2
def calculate_frequency(alphabet_2):
    total_count = sum(alphabet_2.values())
    for a, b, in alphabet_2.items():
        alphabet_2[a] = (alphabet_2[a]/ total_count)
    return alphabet_2


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
dict_1 = count_letters(main_str)
dict_2 = calculate_frequency(dict_1)
#print(dict_1)
#print(dict_2)
# dict_3 = {k: v for v, k in dict_2.items()}
for key, value in dict_2.items():
    print(f'{key}: {value:.2f}')
# result = '\n'.join(f'{v}: {k}' for k, v in dict_2.items())
# print(result)

#частота высчитывается некорректно