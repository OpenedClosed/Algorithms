"""
Вечером ребята решили поиграть
в игру «Большое число».
Даны числа. Нужно определить,
какое самое большое
число можно из них составить.
"""

def checker(number1, number2):
    return int(number2+number1) < int(number1+number2)

def get_the_highest(array):
    for i in range(1, len(array)):
        item = array[i]
        j = i
        while j > 0 and checker(item, array[j-1]):
            array[j] = array[j-1]
            j-=1
        array[j] = item
    return array

if __name__ == "__main__":
    length = int(input())
    array = input().split()[:length]
    res = get_the_highest(array)
    print(''.join(res))