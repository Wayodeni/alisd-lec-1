from random import choice, shuffle


def quicksort(lst):
   if len(lst) <= 1:
       return lst
   else:
       q = choice(lst)  # выбрать случайный элемент
       smaller_elements = []
       bigger_elements = []
       equal_elements = []
       for n in lst:
           if n < q:
               smaller_elements.append(n)
           elif n > q:
               bigger_elements.append(n)
           else:
               equal_elements.append(n)
       return quicksort(smaller_elements) + equal_elements + quicksort(bigger_elements)

a = [i for i in range(5)]
print('Исходный список: ', a)
shuffle(a)
print('Перемешанный список: ', a)
print('Результат сортировки: ', quicksort(a))