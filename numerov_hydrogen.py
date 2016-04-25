import pylab as lab
import math


def g(x, n, l):  # g(x, n, l)
    return 2*(-1/(2 * n * n) + 1/x - l * (l + 1)/(2 * x * x))


def integrate(y, a, b, h):
    sum = 0

    for i in range(a, b):
        sum += h / 2 * (y[i] + y[i + 1])

    return sum


def max_index(a):
    m = max(a)
    for i, j in enumerate(a):
        if j == m:
            return i


def prob(y):
    new = []
    for item in y:
        new.append(item * item)

    return new


def normal_const(y, h):
    return 1 / math.sqrt(integrate(prob(y), 0, len(y) - 2, h))


def normalize(y, h):
    new = []
    const = normal_const(y, h)
    for (i, item) in enumerate(y):
        new.append(item * const)

    return new


h = (10**(-1))  # vzdálenost x(n + 1) - x(n), diference
x_min = h  # malá hodnota v blízkosti nuly
x_max = 15.0  # maximální hodnota v poloze
n = 1  # hlavní kvantové číslo
l = 0  # vedlejší kvantové číslo
a = 10**(-3)  # libovolně zvolené y(n)

x = [x_max - h, x_max]  # počáteční hodnoty v poloze
y = [a, 0]  # počáteční hodnoty vlnové funkce

c_x = x_max - 2 * h  # počáteční hodnota polohy pro první iteraci

y0 = y[0]
y1 = y[1]

while c_x > x_min: # procházet od x(max) do x(min)
    # nová hodnota pro Numerovu metodu
    y2 = (2 * y1 * (1 - 5 * h**2 * g(c_x + h, n, l)/12) - y0 * (1 + h**2 * g(c_x + 2 * h, n, l)/12))/(1 + h**2 * g(c_x, n, l)/12)

    # předefinování hodnot y(n) a y(n - 1) pro novou iteraci
    y0 = y1
    y1 = y2

    # uložit hodnoty do pole
    x.insert(0, c_x)
    y.insert(0, y2 * y2)

    c_x -= h # přičíst diferenci

# Plot
lab.plot(x, y)
lab.xlabel("x")
lab.ylabel("$|\psi|^2$")
lab.show()
