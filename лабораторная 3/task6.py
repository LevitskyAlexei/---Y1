list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

a = max(list_numbers)# TODO Оформить решение
b = list_numbers.index(a)
c = list_numbers[-1]

list_numbers[b] = c
list_numbers[-1] = a

print(list_numbers)
