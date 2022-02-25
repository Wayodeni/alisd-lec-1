from random import shuffle


def exchange_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

a = [i for i in range(5)]
print('Исходный список: ', a)
shuffle(a)
print('Перемешанный список: ', a)
exchange_sort(a)
print('Результат сортировки: ', a)