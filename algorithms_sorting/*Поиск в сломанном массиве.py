# ID: 81717023
"""
Алла ошиблась при копировании из одной структуры данных в другую.
Она хранила массив чисел в кольцевом буфере.
Массив был отсортирован по возрастанию,
и в нём можно было найти элемент за логарифмическое время.
Алла скопировала данные из кольцевого буфера в обычный массив,
но сдвинула данные исходной отсортированной последовательности.
Теперь массив не является отсортированным.
Тем не менее, нужно обеспечить возможность
находить в нем элемент за O(log(n)).
Можно предполагать, что в массиве только уникальные элементы.
"""
from typing import Any, List


def broken_search(broken_loop: List[Any], element: int) -> int:
    """
    Функция поиска индекса элемента в массиве
    вида разорванного кольцевого буфера
    за алгоритмическую сложность O(log(n)).
    """
    left, right = 0, len(broken_loop)-1

    while right >= left:
        mid = (left + right) // 2

        if broken_loop[mid] == element:
            return mid

        if broken_loop[mid] <= broken_loop[right]:
            if broken_loop[mid] < element <= broken_loop[right]:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if broken_loop[left] <= element < broken_loop[mid]:
                right = mid - 1
            else:
                left = mid + 1
    return -1


def test():
    """
    Проврека работоспособности алгоритма
    на тестовых данных.
    """
    data1 = [5, 6, 7, 9, 0, 2, 3, 4]
    number1 = 3
    numbers_position1 = broken_search(broken_loop=data1, element=number1)
    expected_position1 = 6
    assert numbers_position1 == expected_position1

    data2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]
    number2 = 1
    numbers_position2 = broken_search(broken_loop=data2, element=number2)
    expected_position2 = 0
    assert numbers_position2 == expected_position2


if __name__ == "__main__":
    test()
