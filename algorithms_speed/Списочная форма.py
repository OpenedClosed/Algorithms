"""
Вася просил Аллу помочь решить задачу. На этот раз по информатике.
Для неотрицательного целого числа X списочная форма –— это массив его цифр слева направо.
К примеру, для 1231 списочная форма будет [1,2,3,1].
На вход подается количество цифр числа Х, списочная форма
неотрицательного числа Х и неотрицательное число K. Числа К и Х не превосходят 10000.
Нужно вернуть списочную форму числа X + K.
"""
import sys

length = int(input())
numbers = (sys.stdin.readline().rstrip())
sum_with = int(input())
int_from_numbers = int(numbers.replace(' ', ''))
print(*str(int_from_numbers + sum_with))

