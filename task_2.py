# Задача 2: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернутывверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.

n = int(input("Введите количество монет: "))
tails = 1
heads = 0
count_t = 0
count_h = 0
for i in range(n):
    num = int(input())
    if num == tails:
        count_t += 1
    elif num == heads:
        count_h += 1
print(min(count_t, count_h))

