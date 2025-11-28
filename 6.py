"""
Команды:

forward(10) Вперед на 10
backward(10) Назад на 10

right(90) Направо на 90 градусов
left(90) Налево на 90 градусов

goto(x, y) Иди на x, y
dot(3) Точка ширины 3
"""


#Пишем всегда
from turtle import *
tracer(0)
k = 10 # Множитель (для forward, backward и точек)
goto(0 * k, 0 * k) # Если рисунок выходит за границы, можно сдвинуть

#Алгоритм из условия
right(90)

for i in range(3):
    forward(15 * k)
    right(90)
    forward(20 * k)
    right(90)
up()

forward(7 * k)
right(90)
forward(13 * k)
left(90)

down()
for i in range(2):
    forward(10 * 10)
    left(90)
    forward(17 * 10)
    left(90)

# Рисуем точки. x, y выбирать так, чтобы покрывали весь рисунок
up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * k, y * k)
        dot(3)
done()