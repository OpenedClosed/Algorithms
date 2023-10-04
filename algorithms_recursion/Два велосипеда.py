"""
Вася решил накопить денег на два одинаковых велосипеда — себе и сестре.
У Васи есть копилка, в которую каждый день он может добавлять деньги
(если, конечно, у него есть такая финансовая возможность).
В процессе накопления Вася не вынимает деньги из копилки.
У вас есть информация о росте Васиных накоплений
— сколько у Васи в копилке было денег в каждый из дней.
Ваша задача — по заданной стоимости велосипеда определить
первый день, в которой Вася смог бы купить один велосипед,
и первый день, в который Вася смог бы купить два велосипеда.
"""

amount = int(input())
saving_list_str = input().split()[:amount]
saving_list_int = list(map(int, saving_list_str))
price = int(input())

def expected_day(saving, price, left, right):
    if right <= left:
        return -1
    
    mid = (left + right) // 2
    
    if int(saving[mid]) >= price and int(saving[mid-1]) < price:
        return mid + 1

    if right - left == 1:
        if int(saving[mid]) >= price: 
            return mid + 1
        elif int(saving[mid]) == price:
            return mid + 1
        elif int(saving[right]) >= price: 
            return right + 1
        else:
            return -1

    if price <= int(saving[mid]):
        return expected_day(saving, price, left, mid)
    else:
        return expected_day(saving, price, mid, right)


if __name__ == "__main__":
    first_day = expected_day(saving_list_int, price, 0, len(saving_list_int) - 1)
    if first_day == -1:
        result = [first_day] * 2
    else:
        result = [first_day, expected_day(saving_list_int, price * 2, first_day, len(saving_list_int) - 1)]
    print(*result)