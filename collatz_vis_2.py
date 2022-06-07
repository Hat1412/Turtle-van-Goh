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
SCALE = 5
t.speed(0)
s.bgcolor("#000000")

num = -670

for j in range(2, 500):
    print(j)
    t.penup()
    x, y = num, -360
    t.goto(x, y)
    t.pendown()
    num += 10
    if (num > 670): num = -670

    for i in collatz(j):
        if i % 2 == 0:
            t.color("#FF0000")
            x += SCALE
            y += SCALE

        if i % 2 != 0:
            t.color("#0000FF")

            x -= SCALE
            y += SCALE

        t.goto(x, y)


def get_pos(x, y):
    print(x, y)


s.onclick(get_pos)
print("DOne")
done()
