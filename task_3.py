# TODO написать функцию для получения списка уникальных целых чисел
#from random import randint


#def get_unique_list_numbers(start=-10, stop=10, size=15):
#    list_of_numbers = [randint(start, stop) for _ in range(size+1)]
#    count = 1
#    while len(list_of_numbers) != len(set(list_of_numbers)):
#        list_of_numbers = [randint(start, stop) for _ in range(size)]
#        count += 1
#    print(count)
#    return list_of_numbers



#list_unique_numbers = get_unique_list_numbers(14)
#print(list_unique_numbers)
#print(len(list_unique_numbers) == len(set(list_unique_numbers)))

from random import randint
from time import time

def get_unique_list_numbers(start=-10, stop=10, size=15):
    list_of_numbers = []
    while len(list_of_numbers) < size:
        number = randint(start, stop)
        if stop - start >= size:
            if number not in list_of_numbers:
                list_of_numbers.append(number)
        return list_of_numbers
list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))

