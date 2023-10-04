"""
Гоша любит играть в игру «Подпоследовательность»:
даны 2 строки, и нужно понять, является ли первая
из них подпоследовательностью второй. Когда строки
достаточно длинные, очень трудно получить ответ на этот вопрос,
просто посмотрев на них. Помогите Гоше написать функцию,
которая решает эту задачу.
"""

def is_subsequence(letters, sequence):
    start = -1
    for letter in letters:
        # print(f'пытаемся найти символ -{letter}- начиная с символа номер: {start + 1}')
        start = sequence.find(letter, start + 1)
        if start == -1:
            return False
    return True
        
   
if __name__ == "__main__":
    letters = input()
    sequence = input()
    print(is_subsequence(letters, sequence))
