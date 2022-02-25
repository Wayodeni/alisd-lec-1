from random import shuffle


def shell_sort(data):
    last_index = len(data)
    step = len(data)//2
    while step > 0:
        for i in range(step, last_index, 1):
            j = i
            delta = j - step
            while delta >= 0 and data[delta] > data[j]:
                data[delta], data[j] = data[j], data[delta]
                j = delta
                delta = j - step
        step //= 2
    return data

a = [i for i in range(5)]
print('Исходный список: ', a)
shuffle(a)
print('Перемешанный список: ', a)
print('Результат сортировки: ', shell_sort(a))