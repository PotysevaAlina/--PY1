def get_count_char(str_):
    new_dict = {}
    new_str_ = str_.lower()
    for dict_ in new_str_:
        if new_dict.get(dict_) == None:
                if dict_.isalpha() == True:
                    new_dict.setdefault(dict_, 1)
        else:
            new_dict[dict_] = new_dict[dict_] + 1

    return new_dict




# TODO посчитать количество каждой буквы в строке в аргументе str_

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))


