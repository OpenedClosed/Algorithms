"""
Васе нужно распечатать свой список дел на сегодня.
Помогите ему: напишите функцию, которая печатает все его дела.
Внимание: в этой задаче не нужно считывать входные данные.
Нужно написать только функцию, которая принимает на вход голову списка
и печатает его элементы. Ниже дано описание структуры, которая задаёт узел списка.
"""

LOCAL = True

if LOCAL:
    class Node:  
        def __init__(self, value, next_item=None):  
            self.value = value  
            self.next_item = next_item

def solution(node):
    while node:
        print(node.value)
        node = node.next_item
    pass

def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    solution(node0)

if __name__ == '__main__':
    test()