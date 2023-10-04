"""
Чтобы подготовиться к семинару,
Гоше надо прочитать статью по эффективному менеджменту.
Так как Гоша хочет спланировать день заранее,
ему необходимо оценить сложность статьи.
Он придумал такой метод оценки:
берётся случайное предложение из текста и в нём ищется самое длинное слово.
Его длина и будет условной сложностью статьи.
Помогите Гоше справиться с этой задачей.
"""
import sys

letters = int(input())
words = (sys.stdin.readline().rstrip()).split()
words_length = []
for i in range(len(words)):
    words_length.append(len(words[i]))
max_length = max(words_length)
max_index = words_length.index(max_length)
print(f'{words[max_index]}\n{max_length}')