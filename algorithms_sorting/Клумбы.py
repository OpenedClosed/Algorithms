"""
Алла захотела, чтобы у неё под окном были узкие клумбы с тюльпанам.
На схеме земельного участка клумбы обозначаются просто горизонтальными отрезками,
лежащими на одной прямой. Для ландшафтных работ было нанято n садовников.
Каждый из них обрабатывал какой-то отрезок на схеме.
Процесс был организован не очень хорошо, иногда один и тот же отрезок
или его часть могли быть обработаны сразу несколькими садовниками.
Таким образом, отрезки, обрабатываемые двумя разными садовниками, сливаются в один.
Непрерывный обработанный отрезок затем станет клумбой. Нужно определить границы будущих клумб.
Рассмотрим примеры.
Пример 1:
Два одинаковых отрезка 
[7,8] и [7,8] сливаются в один, но потом их накрывает отрезок [6,10]. Таким образом, имеем две клумбы с координатами [2,3] и [6,10].
Пример 2:
Отрезки [2,3], [3,4] и [3,4] сольются в один отрезок [2,4]. Отрезок [5,6]
ни с кем не объединяется, добавляем его в ответ.
"""

def get_flowerbed(sorted_coord):
    result = []

    for coord in range(len(sorted_coord)-1):
        if sorted_coord[coord][1] >= sorted_coord[coord+1][0]:
            sorted_coord[coord+1][0] = sorted_coord[coord][0]
            sorted_coord[coord+1][1] = max(sorted_coord[coord][1], sorted_coord[coord+1][1])

        else:
            result.append(sorted_coord[coord])
    result.append(sorted_coord[-1])
    return result        
 
if __name__ == "__main__":
    amount = int(input())
    coordinates = []
    for _ in range(amount):
        coordinates.append(list(map(int, input().split())))
    sorted_coord = list(sorted(coordinates))
    lst = get_flowerbed(sorted_coord)
    for i in lst:
        print(*i)
