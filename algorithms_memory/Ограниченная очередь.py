"""
Астрологи объявили день очередей ограниченного размера. 
Тимофею нужно написать класс MyQueueSized,
который принимает параметр max_size,
означающий максимально допустимое количество элементов в очереди.
Помогите ему —– реализуйте программу,
которая будет эмулировать работу такой очереди. Функции,
которые надо поддержать, описаны в формате ввода.
"""

class MyQueueSized():
    def __init__(self, n):
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0 

    def is_empty(self):
        return self.size == 0

    def pop(self):
        if self.is_empty():
            return None
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x 

    def push(self, x):
        if self.size != self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
        else:
            print('error')

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[self.head]

if __name__ == '__main__':
    command_num = int(input())
    max_size = int(input())
    new_queue = MyQueueSized(max_size)
    for i in range(command_num):
        cmd = input().split()
        if cmd[0] == 'pop':
            print(new_queue.pop())
        elif cmd[0] == 'push':
            new_queue.push(int(cmd[1]))
        elif cmd[0] == 'peek':
            print(new_queue.peek())
        elif cmd[0] == 'size':
            print(new_queue.size)