from math import sqrt
from math import pi
from math import exp


def avg(iterator):
    return sum(iterator) / len(iterator)


def std_dev(iterator, population = False):
    _avg = avg(iterator)
    std_dev = 0

    for i in range(len(iterator)):
        std_dev += (iterator[i] - _avg) * (iterator[i] - _avg)

	if population:
	    return sqrt(std_dev / (len(iterator)))

    return sqrt(std_dev / (len(iterator)-1))


def std_norm_distrib(x):
    return 1 / sqrt(2 * pi) * exp(-.5 * x * x)


def general_norm_distrib(x, micro, sigma):
    sigma *= sigma

    return 1 / sigma * std_norm_distrib((x - micro) / sigma)
