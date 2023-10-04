"""
Представьте себе онлайн-игру для поездки в метро:
игрок нажимает на кнопку, и на экране появляются три случайных числа.
Если все три числа оказываются одной чётности, игрок выигрывает.
Напишите программу, которая по трём числам определяет, выиграл игрок или нет.
"""
numbers = list(map(int, input().split()[:3]))
def even_or_odd(values):
    counter = 0
    for value in values:
        if value % 2 == 0:
            counter += 1
    if counter in range(1, 3):
        return "FAIL"
    return "WIN"
print(even_or_odd(numbers))
