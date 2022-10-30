# TODO реализовать функцию удаления элемента из списка по индексу
def delete(list_, index = None):
    if index != None:
        for index in list_:
            del list_[index + 1]
            return list_
    else:
       del list_[-1]
       return list_

print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
