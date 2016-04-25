import pylab as lab
import math


def integrate(y, a, b, h):
    sum = 0

    for i in range(a, b):
        sum += h / 2 * (y[i] + y[i + 1])

    return sum


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


def g(x, n):  # g(x, n), x - parametr vlnové funkce, n - přirozená hodnota číslující energetický stav
    return 2*(n + 0.5) - x*x


h = (10**(-3))  # vzdálenost x(n + 1) - x(n), diference
x_min = -6.0  # rozpětí grafu a zároveň hodnota, kde by měla být vlnová funkce nulová
x_max = - x_min  # maximální hodnota

n = 6  # hodnota energetického stavu, n = 0, 1, 2, 3, 4,...
a = 10**(-6)  # libovolná hodnota volnové funkce y(n)

x = [x_min, x_min + h]  # počáteční hodnoty pro polohu
y = [0, a]  # počáteční hodnoty pro vlnovou funkci

h_x = x_min + 2*h  # počáteční hodnota x pro iteraci

y0 = y[0]  # pomocné proměnné pro numerovu metodu
y1 = y[1]  # -- || --

while h_x < x_max: # procházet od x(min) do x(max)
    # y(n + 1) - nová hodnota v numerově metodě
    y2 = (2 * y1 * (1 - 5 * h**2 * g(h_x - h, n)/12)
          - y0 * (1 + h**2 * g(h_x - 2 * h, n)/12))/(1 + h**2 * g(h_x, n)/12)

    # předefinování hodnot y(n) a y(n - 1) pro novou iteraci
    y0 = y1
    y1 = y2

    # uložit hodnoty do pole
    x.append(h_x)
    y.append(y2)

    h_x += h  # přičíst diferenci

# Vykreslit
lab.plot(x, normalize(y, h))
lab.xlabel("x")
lab.ylabel("$\psi$")
lab.show()
