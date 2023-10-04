# ID: 72108302
"""
Игра «Тренажёр для скоростной печати» представляет
собой поле из клавиш 4x4.
В нём на каждом раунде появляется конфигурация цифр и точек.
На клавише написана либо точка, либо цифра от 1 до 9.
В момент времени t игрок должен одновременно нажать на все клавиши,
на которых написана цифра t.
Гоша и Тимофей могут нажать в один момент времени на k клавиш каждый.
Если в момент времени t нажаты все нужные клавиши,
то игроки получают 1 балл.
Найдите число баллов, которое смогут заработать
Гоша и Тимофей, если будут нажимать на клавиши вдвоём.
"""

def touch_the_button(fingers, field):
    """Функция, определяющая получит ли пара 
    игрков балл при попытке нажать на нужные
    клавиши на игровом поле"""
    score = 0
    counter = {}
    for line in field:
        for num in line:
            counter[num] = counter.get(num, 0) + 1

    for value in counter:
        if counter[value] <= fingers and value != '.':
            score += 1
    return score

if __name__ == "__main__":
    players_fingers = 2 * int(input())
    game_field = []
    for i in range(4):
        row = game_field.append(input()[:4])
    print(
        touch_the_button(
            fingers=players_fingers, field=game_field
        )
    )
