"""
Мама Васи хочет знать, что сын планирует делать и когда.
Помогите ей: напишите функцию solution,
определяющую индекс первого вхождения
передаваемого ей на вход значения в связном списке,
если значение присутствует.
Внимание: в этой задаче не нужно считывать входные данные.
Нужно написать только функцию, которая принимает на вход
голову списка и искомый элемент,
а возвращает целое число — индекс найденного элемента или -1.
"""

LOCAL = True

if LOCAL:
    class Node:  
        def __init__(self, value, next_item=None):  
            self.value = value  
            self.next_item = next_item

def solution(node, elem):
    idx = 0
    current_node = node
    while current_node.value != elem:
        idx += 1
        if current_node.next_item == None:
            return -1
        current_node = current_node.next_item
    return idx

def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    idx = solution(node0, "node2")
    print(idx)
    assert idx == 2

if __name__ == '__main__':
    test()