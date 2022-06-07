import random
from matplotlib import pyplot as plt
from turtle import *
import turtle

like = [
    "Solarize_Light2",
    "dark_background",
    "seaborn-deep",
    "seaborn-muted",
    "seaborn-dark",
    "bmh",
    "seaborn-ticks",
    "fast",
]

a = random.choice(like)
plt.style.use("bmh")
print(a)


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


# ___________________________________________________Test__________________________________________________________________

# for i in range(10 ** 5, 10 ** 8):
#     if not collatz(i):
#         print(i)
#         print("Found X")


# _________________________________________________Graph___________________________________________________________________
d = {}

for i in range(10, 100):
    d[i] = collatz(i)

plt.plot([1 for _ in range(110)])

for ind, val in d.items():
    plt.plot(val)

plt.show()

# _____________________________________________ Vizualisation  _____________________________________________

