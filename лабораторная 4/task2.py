
def get_count_char(str_: str):  # TODO посчитать количество каждой буквы в строке в аргументе str_
    str_ = str_.lower()
    letter_dic = {}
    for letter in str_:
        if not letter.isalpha():
            continue
        letter_dic[letter] = letter_dic.get(letter, 0) + 1
    return letter_dic


def get_count_percent(lettrt_dic: dict):
    new_dic = {}
    summ = sum(lettrt_dic.values())
    for key in lettrt_dic:
        new_dic[key] = (lettrt_dic[key] / summ) * 100
    return new_dic


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов.
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
