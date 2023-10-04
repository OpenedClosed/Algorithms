# ID: 74442512
"""
Гоша реализовал структуру данных Дек,
максимальный размер которого определяется заданным числом.
Методы push_back(x), push_front(x), pop_back(), pop_front()
работали корректно. Но, если в деке было много элементов,
программа работала очень долго. Дело в том,
что не все операции выполнялись за O(1).
Помогите Гоше! Напишите эффективную реализацию.
Внимание: при реализации используйте кольцевой буфер.
"""

class EmptyError(Exception):
    """Ошибка при попытке вернуть
    элемент из пустого стека"""
    pass


class FullError(Exception):
    """Ошибка при попытке добавить
    элемент в заполненный стек"""
    pass


class DequeSized:
    """Класс дек, определяющий
    методы двухсторонней очереди
    с ограниченным размером"""
    def __init__(self, max_amount):
        self.__items = [None] * max_amount
        self.__max_amount = max_amount
        self.__head = 0
        self.__tail = 0
        self.__size = 0

    def is_empty(self):
        """Метод, отвечающий за проверку спика на пустоту"""
        return self.__size == 0

    def push_front(self, new_left_element):
        """Метод, отвечающий за вставку
        нового элемента вперед (влево)"""
        if self.__size != self.__max_amount:
            if self.__size != 0:
                self.__head = (
                    self.__head + (self.__max_amount - 1)
                ) % self.__max_amount
            self.__items[self.__head] = new_left_element
            self.__size += 1
        else:
            raise FullError

    def push_back(self, new_right_element):
        """Метод, отвечающий за вставку
        нового элемента назад (вправо)"""
        if self.__size != self.__max_amount:
            if self.__size != 0:
                self.__tail = (self.__tail + 1) % self.__max_amount
            self.__items[self.__tail] = new_right_element
            self.__size += 1
        else:
            raise FullError

    def pop_front(self):
        """Метод, отвечающий за удаление
        существующего элемента, находящегося
        по указателю головы"""
        if self.is_empty():
            raise EmptyError
        prev_head = self.__items[self.__head]
        self.__items[self.__head] = None
        self.__size -= 1
        if self.__size != 0:
            self.__head = (self.__head + 1) % self.__max_amount
        return prev_head

    def pop_back(self):
        """Метод, отвечающий за удаление
        существующего элемента, находящегося
        по указателю хвоста"""
        if self.is_empty():
            raise EmptyError
        prev_tail = self.__items[self.__tail]
        self.__items[self.__tail] = None
        self.__size -= 1
        if self.__size != 0:
            self.__tail = (
                self.__tail + (self.__max_amount - 1)
            ) % self.__max_amount
        return prev_tail


def operation_definition(number, size):
    """Функция, выполняющая необходимые для
    пользователя действия с деком"""
    new_deque = DequeSized(size)
    for _ in range(number):
        cmd = input().split()
        try:
            if len(cmd) == 2:
                getattr(new_deque, cmd[0])(cmd[1])
            elif len(cmd) == 1:
                result = getattr(new_deque, cmd[0])()
                if result is not None:
                    print(result)
        except EmptyError:
            print('error')
        except FullError:
            print('error')

if __name__ == '__main__':
    command_num = int(input())
    max_size = int(input())
    operation_definition(command_num, max_size)
