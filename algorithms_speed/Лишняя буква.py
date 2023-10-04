"""
Васе очень нравятся задачи про строки, поэтому он придумал свою.
Есть 2 строки s и t, состоящие только из строчных букв.
Строка t получена перемешиванием букв строки s и добавлением 1 буквы в случайную позицию.
Нужно найти добавленную букву.
"""
a = ''.join(sorted(input()))
b = ''.join(sorted(input()))

length = min(len(a), len(b))
index = 0
for i in range(length):
    if a[i] != b[i]:
        break
    index += 1

if len(a) > length:
    print(a[index])
if len(b) > length:
    print(b[index])
