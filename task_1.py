# Задача 1. Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача: арбузов слишком много и
# он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9

n = int(input("Введите количество арбузов: "))
mas = int(input())
max = mas
min = mas
for i in range(n - 1):
    mas = int(input())
    if mas > max:
        max = mas
    elif mas < min:
        min = mas
print(max, min)