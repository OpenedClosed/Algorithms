# ID: 72062974
"""
Тимофей ищет место, чтобы построить себе дом.
Улица, на которой он хочет жить, имеет длину n,
то есть состоит из n одинаковых идущих подряд участков.
Каждый участок либо пустой, либо на нём уже построен дом.
Общительный Тимофей не хочет жить далеко от других людей на этой улице.
Поэтому ему важно для каждого участка знать расстояние
до ближайшего пустого участка. Если участок пустой,
эта величина будет равна нулю — расстояние до самого себя.
Помогите Тимофею посчитать искомые расстояния.
Для этого у вас есть карта улицы.
Дома в городе Тимофея нумеровались в том порядке,
в котором строились, поэтому их номера на карте никак не упорядочены.
Пустые участки обозначены нулями.
"""

def closer_zero(numbers):
    """"Функция, находящая расстояния от 
    определнного числа в массиве до ближайшего
    к нему нуля"""
    zero_positions = [
        i for i, number in enumerate(numbers) if number == 0
    ]
    distance = []
    begining = 0
    end = 0
    i = 0

    while (i >= begining and i <= zero_positions[end] + 1):
        if begining == zero_positions[-1]:
            while i <= len(numbers) - 1:
                distance.append(i - begining)
                i += 1
            break
        while numbers[i] == 0:
            distance.append(0)
            i += 1
            begining = zero_positions[end]
            if zero_positions[end] != zero_positions[-1]:
                end += 1
            break
        while i <= zero_positions[0]:
            distance.append(zero_positions[0] - i)
            i += 1
        middle = (zero_positions[end] + begining) // 2
        while i <= middle:
            distance.append(i - begining)
            i += 1
        while (i > middle and i <= zero_positions[end]):
            distance.append(zero_positions[end] - i)
            i += 1
        begining = zero_positions[end]
        if zero_positions[end] != zero_positions[-1]:
            end += 1

    return distance

if __name__ == "__main__":
    amount_of_districts = int(input())
    house_numbers = list(map(int, input().split()[:amount_of_districts]))
    print(*closer_zero(numbers=house_numbers))
