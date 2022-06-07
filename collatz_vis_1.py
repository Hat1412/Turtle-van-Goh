import random
from turtle import *

def collatz(n):
    num = n
    l = []
    while num != 1:
        if num % 2 == 0:
            num /= 2
        elif num % 2 != 0:
            num = 3 * num + 1

        l.append(num)

    return l

t = Turtle()
s = Screen()
SCALE = 10
t.speed(0)
s.bgcolor("#000000")

for j in range(2, 500):
    print(j)
    t.penup()
    x, y = 0, -360
    t.goto(x, y)
    t.pendown()
    t.color(random.choice(
            ["#FF0000",
            "#0000FF",
            "#00FF00",
            "#FFD700",
            "#FFC0CB",
            "#FFA500",
            "#00FFFF",
            "#FF00FF",
            "#C0C0C0",
            "#B87333"]))

    for i in collatz(j):
        if i % 2 == 0:
            x += SCALE
            y += SCALE

        if i % 2 != 0:
            x -= SCALE
            y += SCALE

        t.goto(x, y)


def get_pos(x, y):
    print(x, y)


s.onclick(get_pos)
print("DOne")
done()
