# ID: 81800724
"""
Тимофей решил организовать соревнование по спортивному
программированию, чтобы найти талантливых стажёров.
Задачи подобраны, участники зарегистрированы, тесты написаны.
Осталось придумать, как в конце соревнования будет определяться победитель.
Каждый участник имеет уникальный логин. Когда соревнование закончится,
к нему будут привязаны два показателя: количество решённых задач Pi
и размер штрафа Fi. Штраф начисляется за неудачные попытки и время,
затраченное на задачу.
Тимофей решил сортировать таблицу результатов следующим образом:
при сравнении двух участников выше будет идти тот,
у которого решено больше задач.
При равенстве числа решённых задач первым идёт участник с меньшим штрафом.
Если же и штрафы совпадают, то первым будет тот, у которого логин
идёт раньше в алфавитном (лексикографическом) порядке.
"""
from collections import namedtuple
from typing import Any, List


def reverse_priority(first_person: List[Any]) -> List[Any]:
    """
    Функция, определяющая кто
    из участинков окажется ниже
    другого в таблице.
    """
    return -first_person.tasks, first_person.penalties, first_person.name


def quick_sorting(data: List[Any], left: int, right: int) -> List[Any]:
    """
    Функция, реализующая алгоритм
    быстрой сортировки без затрат
    дополнительной памяти.
    """
    if left >= right:
        return data

    pivot = data[(left + right) // 2]
    left_coef_coord, righ_coef_coord = left, right
    pivot_reverse_priority = reverse_priority(pivot)
    while left_coef_coord < righ_coef_coord:

        while reverse_priority(data[left_coef_coord]) < pivot_reverse_priority:
            left_coef_coord += 1

        while reverse_priority(data[righ_coef_coord]) > pivot_reverse_priority:
            righ_coef_coord -= 1

        data[left_coef_coord], data[righ_coef_coord] = (
            data[righ_coef_coord], data[left_coef_coord]
        )

    quick_sorting(data, left=left, right=left_coef_coord)
    quick_sorting(data, left=righ_coef_coord+1, right=right)
    return data


if __name__ == "__main__":
    amount = int(input())
    data = []
    Person = namedtuple('Person', 'name tasks penalties')
    for _ in range(amount):
        person = input().split()
        data.append(Person(person[0], int(person[1]), int(person[2])))
    sorted_data = quick_sorting(data=data, left=0, right=len(data)-1)
    print('\n'.join([i.name for i in sorted_data]))
