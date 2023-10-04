"""
Дана матрица. Нужно написать функцию,
которая для элемента возвращает всех его соседей.
Соседним считается элемент, находящийся от текущего на одну ячейку
влево, вправо, вверх или вниз. Диагональные элементы соседними не считаются.
"""
row = int(input())
col = int(input())
matrix = [(list(map(int, input().split()))[:col]) for j in range(row)]
number_row = int(input())
number_col = int(input())
neighbors = []

neighbors.extend(
    [
        matrix[number_row][number_col - col + 1],
        matrix[number_row][number_col - 1],
        matrix[number_row - row + 1][number_col],
        matrix[number_row - 1][number_col],
    ]
)
if number_row == 0:
    neighbors.remove(matrix[row - 1][number_col])
if number_row == row - 1:
    neighbors.remove(matrix[0][number_col])
if number_col == 0:
    neighbors.remove(matrix[number_row][number_col - 1])
if number_col == col - 1:
    neighbors.remove(matrix[number_row][0])

print(*(sorted(neighbors)))