"""
Рита и Гоша играют в игру. У Риты есть n фишек,
на каждой из которых написано количество очков.
Сначала Гоша называет число k, затем Рита должна выбрать две фишки,
сумма очков на которых равна заданному числу.
Рите надоело искать фишки самой,
и она решила применить свои навыки программирования для решения этой задачи.
Помогите ей написать программу для поиска нужных фишек.
"""
length = int(input())
list_of_numbers = list(map(int, input().split()))
target = int(input())
def two_sum():
    for i in range(0, length):
        for j in range(i+1, length):
            if list_of_numbers[i] + list_of_numbers[j] == target:
                return list_of_numbers[i], list_of_numbers[j]
if two_sum() == None:
    print(two_sum())
else:
    print(*two_sum())
