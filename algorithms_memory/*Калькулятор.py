# ID: 74343078
"""
Задание связано с обратной польской нотацией.
Она используется для парсинга арифметических выражений.
Еще её иногда называют постфиксной нотацией.
"""

SIGNS_OPERATIONS = {
    '+': lambda elem1, elem2: elem1 + elem2,
    '-': lambda elem1, elem2: elem1 - elem2,
    '*': lambda elem1, elem2: elem1 * elem2,
    '/': lambda elem1, elem2: elem1 // elem2
}

class EmptyError(Exception):
    """Ошибка при попытке вернуть
    элемент из пустого стека"""

    def __init__(
        self,
        message="Нельзя вернуть элемент из пустого стека"
    ):
        self.message = message
        super().__init__(self.message)


class SimpleStack:
    """Класс стек, поддерживающий лишь
    методы добавления и удаления элементов"""

    def __init__(self):
        self.__items = []

    def get_result(self):
        """Возвращает результат"""
        return self.__items[-1]

    def is_empty(self):
        """Проверка на пустоту стека"""
        return len(self.__items) == 0

    def pop(self):
        """Забрать элемент из начала"""
        if self.is_empty():
            raise EmptyError
        return self.__items.pop()

    def push(self, element: int):
        """Добавить элемент в начало"""
        self.__items.append(element)


def calculate_this(list_of_elem):
    """Функция, реализующая алгоритм
    калькуляции по обратной польской
    нотации"""
    stack = SimpleStack()
    i_elem = 0
    if len(list_of_elem) in (1, 2):
        return list_of_elem[-1]
    while i_elem < len(list_of_elem):
        while list_of_elem[i_elem] not in SIGNS_OPERATIONS:
            stack.push(int(list_of_elem[i_elem]))
            i_elem += 1
        mid_result = SIGNS_OPERATIONS[list_of_elem[i_elem]](
            elem2=stack.pop(), elem1=stack.pop()
        )
        stack.push(mid_result)
        i_elem += 1
    return stack.get_result()

if __name__ == "__main__":
    list_of_elements = input().split()
    print(calculate_this(list_of_elements))
