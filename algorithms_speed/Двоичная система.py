"""
Тимофей записал два числа в двоичной системе счисления
и попросил Гошу вывести их сумму, также в двоичной системе.
Встроенную в язык программирования возможность
сложения двоичных чисел применять нельзя.
Помогите Гоше решить задачу.
Решение должно работать за O(N),
где N –— количество разрядов максимального числа на входе.
"""
a = str(input())
b = str(input())

length = max(len(a), len(b))
a = a.zfill(length)
b = b.zfill(length)

answer = ''
carry = 0
for i in reversed(range(length)):
    summa = int(a[i]) + int(b[i]) + carry
    carry = 0
    if summa == 0:
        answer += '0'
    if summa == 2:
        answer += '0'
        carry = 1
    if summa % 2 == 1:
        answer += '1'
        if summa == 3:
            carry = 1
if carry != 0:
    answer += str(carry)
print(answer[::-1])
