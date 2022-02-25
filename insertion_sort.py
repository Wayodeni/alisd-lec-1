from random import shuffle


def insertion_sort(lst):
    for i in range(1, len(lst)):
        for j in range(0, i):
            if lst[i] < lst[j]:
                lst[i], lst[j] = lst[j], lst[i]

a = [i for i in range(5)]
print('Исходный список: ', a)
shuffle(a)
print('Перемешанный список: ', a)
insertion_sort(a)
print('Результат сортировки: ', a)