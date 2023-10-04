"""
Рита и Гоша играют в игру. У Риты есть n фишек,
на каждой из которых написано количество очков.
Фишки лежат на столе в порядке неубывания очков на них.
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
    help_volume = set()
    for number in list_of_numbers:
        different = target - number
        if different in help_volume:
            return number, different
        else:
            help_volume.add(number)
            print(help_volume)
if two_sum() == None:
    print(two_sum())
else:
    print(*two_sum())
