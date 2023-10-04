"""
Реализуйте класс StackMaxEffective, поддерживающий операцию
определения максимума среди элементов в стеке.
Сложность операции должна быть O(1).
Для пустого стека операция должна возвращать None.
При этом push(x) и pop() также должны выполняться за константное время.
"""

class StackMaxEffective():
    def __init__(self):
        self.items = []
        self.max = []

    def isEmpty(self):
        return (len(self.items) == 0)

    def pop(self):
        if self.isEmpty():
            print('error')
        else:
            if len(self.max) != 0:
                if self.max[-1] == self.items[-1]:
                    self.max.pop()
            self.items.pop()

    def push(self, x: int):
        if self.isEmpty() or len(self.max) == 0:
            self.max.append(x)
        elif x >= self.max[-1]:
            self.max.append(x)
        self.items.append(x)
    
    def get_max(self):
        if self.isEmpty() or len(self.max) == 0:
            return 'None'
        return self.max[-1]

if __name__ == '__main__':
    n = int(input())
    new_stack = StackMaxEffective()
    for i in range(n):
        cmd = input().split()
        if cmd[0] == 'pop':
            new_stack.pop()
        elif cmd[0] == 'push':
            new_stack.push(int(cmd[1]))
        elif cmd[0] == 'get_max':
            print(new_stack.get_max())