"""
Вот какую задачу Тимофей предложил на собеседовании одному из кандидатов.
Если вы с ней ещё не сталкивались, то наверняка столкнётесь –— она довольно популярная.
Дана скобочная последовательность. Нужно определить, правильная ли она.
Будем придерживаться такого определения:
пустая строка —– правильная скобочная последовательность;
правильная скобочная последовательность, взятая в скобки одного типа,
–— правильная скобочная последовательность;
правильная скобочная последовательность с приписанной слева
или справа правильной скобочной последовательностью —– тоже правильная.
На вход подаётся последовательность из скобок трёх видов: [], (), {}.
Напишите функцию is_correct_bracket_seq, которая принимает на вход скобочную последовательность
и возвращает True, если последовательность правильная, а иначе False.
"""

class Stack():
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
    
OPENING_BR = ('(', '[', '{') 
CLOSING_BR = (')', ']', '}')
PAIRS = {
    ')': '(',
    ']': '[',
    '}': '{'
}

def is_correct_bracket_seq(seq):
    steck = Stack()
    i_elem = 0
    while i_elem < len(list(seq)):
        while seq[i_elem] in OPENING_BR:
            steck.push(seq[i_elem])
            i_elem += 1
            if i_elem > len(list(seq)) - 1:
                return False
        while seq[i_elem] in CLOSING_BR:
            if len(steck.items) != 0 and seq[i_elem]:

                if PAIRS[seq[i_elem]] != steck.items[-1]:
                    return False
                steck.pop()
                i_elem += 1
                if i_elem > len(list(seq)) - 1:
                    break
            else:
                return False
        if i_elem == len(list(seq)) and len(steck.items) != 0:
            return False
    return True
            
if __name__ == '__main__':
    seq = (input())
    print(is_correct_bracket_seq(seq))
