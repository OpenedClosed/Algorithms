"""
Любимый вариант очереди Тимофея — очередь,
написанная с использованием связного списка.
Помогите ему с реализацией. Очередь должна поддерживать выполнение трёх команд:
get() — вывести элемент, находящийся в голове очереди,
и удалить его. Если очередь пуста, то вывести «error».
put(x) — добавить число x в очередь
size() — вывести текущий размер очереди
"""

class Node:  
    def __init__(self, value, next_item=None, prev_item=None):  
        self.value = value  
        self.next_item = next_item
        self.prev_item = prev_item

class MyQueueLinked():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def get(self):
        if self.is_empty():
            return 'error'
        old_head = self.head
        self.head = old_head.next_item
        self.size -= 1
        return old_head.value

    def put(self, x):
        if self.is_empty():
            self.head = Node(x)
            self.tail = self.head
        else:
            old_tail = self.tail
            self.tail = Node(x, prev_item=old_tail)
            old_tail.next_item = self.tail
        self.size += 1


if __name__ == '__main__':
    command_num = int(input())
    queue = MyQueueLinked()
    for i in range(command_num):
        cmd = input().split()
        if cmd[0] == 'get':
            print(queue.get())
        elif cmd[0] == 'put':
            queue.put(int(cmd[1]))
        elif cmd[0] == 'size':
            print(queue.size)