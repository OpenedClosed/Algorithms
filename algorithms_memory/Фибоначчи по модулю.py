"""
Вычислить k последних цифр числа Фибоначчи.
"""

def fibonacсi_last_numbers(n):
    first_second = [1, 1]
    d = 10 ** k
    if n < 2:
        return 1
    n -= 1
    for i in range(n):
        s = (first_second[0] + first_second[1]) % d
        first_second[0] = first_second[1]
        first_second[1] = s
    return first_second[1]

if __name__ == "__main__":
    n, k = map(int, input().split())
    print(fibonacсi_last_numbers(n))