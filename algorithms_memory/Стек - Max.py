"""
Нужно реализовать класс StackMax,
который поддерживает операцию определения максимума
среди всех элементов в стеке.
Класс должен поддерживать операции push(x),
где x – целое число, pop() и get_max().
"""

class StackMax():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return (len(self.items) == 0)

    def pop(self):
        if self.isEmpty():
            print('error')
        else:
            self.items.pop()

    def push(self, x: int):
        self.items.append(x)
    
    def get_max(self):
        if self.isEmpty():
            return 'None'
        return max(self.items)

if __name__ == '__main__':
    n = int(input())
    new_stack = StackMax()
    for i in range(n):
        cmd = input().split()
        if cmd[0] == 'pop':
            new_stack.pop()
        elif cmd[0] == 'push':
            new_stack.push(int(cmd[1]))
        elif cmd[0] == 'get_max':
            print(new_stack.get_max())
