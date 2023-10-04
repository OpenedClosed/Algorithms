"""
На клавиатуре старых мобильных телефонов
каждой цифре соответствовало несколько букв.
Вам известно в каком порядке были нажаты кнопки телефона,
без учета повторов. Напечатайте все комбинации букв,
которые можно набрать такой последовательностью нажатий.
"""

CODE = {
    2:'abc',
    3:'def',
    4:'ghi',
    5:'jkl',
    6:'mno',
    7:'pqrs',
    8:'tuv',
    9:'wxyz'
}

def get_all_combinations(rows):
    res = []
    if len(rows) == 0:
        return ['']
    else:
        next_row = rows.pop()
        pre_combinations = get_all_combinations(rows)
        for pre_combination in pre_combinations:
            for letter in next_row:
                res.append(pre_combination + letter)
    return res

if __name__ == "__main__":
    
    phone_buttons = list(map(int, list(input())))[:10]
    buttons_rows = [CODE[i] for i in phone_buttons]
    res = get_all_combinations(buttons_rows)
    print(*res)
