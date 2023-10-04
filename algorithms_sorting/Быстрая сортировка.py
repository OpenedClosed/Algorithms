"""
Классическая быстрая
сортировка для себя.
"""
import random


def partition(array: list, pivot: int) -> list:
    left = [element for element in array if (element < pivot)]
    right = [element for element in array if (element > pivot)]
    return left, pivot, right

def quick_sorting(data: list) -> list:
    """
    Функция, реализующая алгоритм
    быстрой сортировки без затрат
    дополнительной памяти.
    """
    if len(data) < 2:
        return data
    else:
        pivot = random.choice(data)
        left, center, right = partition(data, pivot)
        return quick_sorting(left) + [center] + quick_sorting(right)

def test():
    """
    Проврека работоспособности алгоритма
    на тестовых данных.
    """
    data = [4, 8, 9, 20, 1, 5, 3, 10]
    sorted_data = quick_sorting(data=data)
    expected = [1, 3, 4, 5, 8, 9, 10, 20]
    assert sorted_data == expected

if __name__ == "__main__":
    test()