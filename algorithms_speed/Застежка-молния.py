"""
Даны два массива чисел длины n.
Составьте из них один массив длины 2n, в котором числа из входных массивов чередуются
(первый — второй — первый — второй — ...).
При этом относительный порядок следования чисел из одного массива должен быть сохранён.
"""
length = int(input())
list_1 = list(map(int, input().split()))
list_2 = list(map(int, input().split()))
result = []
for num in range(length * 2):
    if num % 2 == 0:
        result.append(int(list_1[num // 2]))
    else:
        result.append(int(list_2[(num-1) // 2]))
print(*result)
