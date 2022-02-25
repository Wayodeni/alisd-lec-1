from random import shuffle


def selection_sort(unsorted_lst, index = 0):
    if index == len(unsorted_lst):
        return unsorted_lst
    minimal_element_index = unsorted_lst.index(min(unsorted_lst[index:]))
    unsorted_lst[index], unsorted_lst[minimal_element_index] = unsorted_lst[minimal_element_index], unsorted_lst[index]
    return selection_sort(unsorted_lst, index + 1)

a = [i for i in range(5)]
print('Исходный список: ', a)
shuffle(a)
print('Перемешанный список: ', a)
print('Результат сортировки: ', selection_sort(a))