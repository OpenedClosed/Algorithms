"""
Помогите Васе понять, будет ли фраза палиндромом.
Учитываются только буквы и цифры,
заглавные и строчные буквы считаются одинаковыми.
Решение должно работать за O(N), где N — длина строки на входе.
"""
import sys

words = (sys.stdin.readline().rstrip())
string = ''
for i in words:
    if i.isdigit() or i.isalpha():
        string += i
low_string = string.lower()
length = len(low_string)
print(low_string[:int(length/2)] == low_string[-1:-int(length/2)-1:-1]) 
print(low_string[:int(length/2)])
print(low_string[-1:-int(length/2)-1:-1])
# A man, a plan, a canal: Panama