def get_count_char(str_):
    frequency = {}
    new_str_ = str_.lower()
    for symbol in new_str_:
        if symbol.isalpha():
            frequency[symbol] = frequency.get(symbol, 0) + 1

    return frequency

def percent(elements):
    total = sum(elements.values())
    for i in elements:
        elements[i] = round((elements[i]/total)*100, 2)

    return elements

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

percent(get_count_char(main_str))
print(get_count_char(main_str))
#print(procent(get_count_char(main_str)))


