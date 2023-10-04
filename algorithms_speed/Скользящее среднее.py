"""
Вам дана статистика по числу запросов в секунду к вашему любимому рекомендательному сервису.
Измерения велись n секунд.
В секунду i поступает qi запросов.
Примените метод скользящего среднего с длиной окна k к этим данным и выведите результат.
"""
length = int(input())
list_of_numbers = list(map(int, input().split()))
result = []
K = int(input())
current_sum = sum(list_of_numbers[0:K])
result.append(current_sum/K)
for i in range(0, length-K):
    first_marker = list_of_numbers[i]
    last_marker = list_of_numbers[i+K]
    current_sum -= first_marker
    current_sum += last_marker
    result.append(current_sum/K)
print(*result)