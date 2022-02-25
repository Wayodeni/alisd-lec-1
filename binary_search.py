def binary_search(searchable_element, lst):
    left_element_index = 0
    middle_element_index = len(lst) // 2
    right_element_index = len(lst) 
    while True:
        if searchable_element == lst[middle_element_index]:
            return 'Найденный элемент: {}, Под индексом: {}'.format(searchable_element, middle_element_index)
        elif searchable_element < lst[middle_element_index]:
            right_element_index = middle_element_index
            middle_element_index = (right_element_index + left_element_index) // 2
        elif searchable_element > lst[middle_element_index]:
            left_element_index = middle_element_index
            middle_element_index = (right_element_index + left_element_index) // 2


numbers = [i for i in range(148)]
print('Исходный список: ', numbers)
print(binary_search(70, numbers))