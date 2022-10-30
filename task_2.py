def get_count_char(str_):
    new_dict = {}
    new_str_ = str_.lower()
    for symbol in new_str_:
        if symbol.isalpha():
            if symbol in new_dict:
                new_dict[symbol] += 1
            else:
                new_dict[symbol] = 1

    return new_dict

def procent(new_dict_2):
    sum = 0
    for i in new_dict_2:
        sum = sum + new_dict_2[i]
    for i in new_dict_2:
        new_dict_2[i] = f"{format((new_dict_2[i]/sum)*100,'.2f')} %"

    return new_dict_2

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

procent(get_count_char(main_str))
print(get_count_char(main_str))
#print(procent(get_count_char(main_str)))


