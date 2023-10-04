"""
Гоше дали задание написать красивую сортировку слиянием.
Поэтому Гоше обязательно надо реализовать отдельно
функцию merge и функцию merge_sort.
Функция merge принимает два отсортированных массива,
сливает их в один отсортированный массив и возвращает его.
Если требуемая сигнатура имеет вид merge(array, left, mid, right),
то первый массив задаётся полуинтервалом 
[left,mid)массива array, а второй – полуинтервалом
[mid,right) массива array. 
Функция merge_sort принимает некоторый подмассив,
который нужно отсортировать.
Подмассив задаётся полуинтервалом — его началом и концом.
Функция должна отсортировать передаваемый в неё подмассив,
она ничего не возвращает.
Функция merge_sort разбивает полуинтервал на две половинки
и рекурсивно вызывает сортировку отдельно для каждой.
Затем два отсортированных массива сливаются в один с помощью merge.
"""

def merge(array, left, mid, right):
    left_part = array[left:mid]
    right_part = array[mid:right]
    i = j = 0
    k = left

    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            array[k] = left_part[i]
            i+=1
        else:
            array[k] = right_part[j]
            j+=1
        k+=1

    while i < len(left_part):
        array[k] = left_part[i]
        i+=1
        k+=1
        
    while j < len(right_part):
        array[k] = right_part[j]
        j+=1
        k+=1

    return array


def merge_sort(arr, lf, rg):
    if rg - lf <= 1:
        return

    mid = (lf+rg)//2
    merge_sort(arr, lf, mid)
    merge_sort(arr, mid, rg)
    merge(arr, lf, mid, rg)

# def test():
#     a = [1, 4, 9, 2, 10, 11]
#     b = merge(a, 0, 3, 6)
#     expected = [1, 2, 4, 9, 10, 11]
#     assert b == expected
#     c = [1, 4, 2, 10, 1, 2]
#     merge_sort(c, 0 , 6)
#     expected = [1, 1, 2, 2, 4, 10]
#     assert c == expected
# test()

